from django.shortcuts import render, redirect
from django.http import JsonResponse  # Add this import
from rdflib import Graph, URIRef, RDF, RDFS
from urllib.parse import unquote
import os

def landing_page(request):
    ontologies = os.listdir('ontologies')
    return render(request, 'ontology/landing_page.html', {'ontologies': ontologies})

def load_existing_ontology(request):
    ontology_name = request.POST.get('ontology_name')
    ontology_path = os.path.join('ontologies', ontology_name)
    g = Graph()
    g.parse(ontology_path, format='application/rdf+xml')
    request.session['ontology'] = g.serialize(format='nt')
    return redirect('browse_ontology')

def upload_ontology(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['ontology_file']
        g = Graph()
        g.parse(uploaded_file, format='application/rdf+xml')
        request.session['ontology'] = g.serialize(format='nt')
        return redirect('browse_ontology')
    return render(request, 'ontology/upload.html')

def browse_ontology(request):
    g = Graph()
    g.parse(data=request.session['ontology'], format='nt')
    classes = list(g.subjects(RDF.type, RDFS.Class))
    properties = list(g.subjects(RDF.type, RDF.Property))
    ontology_tree = build_tree(g, classes)
    return render(request, 'ontology/tree.html', {'ontology_tree': ontology_tree, 'ontology_properties': properties})

def class_details(request):
    class_uri = request.GET.get('class_uri')
    g = Graph()
    g.parse(data=request.session['ontology'], format='nt')
    class_uri = URIRef(unquote(class_uri))
    details = {
        'label': str(g.value(class_uri, RDFS.label)),
        'comment': str(g.value(class_uri, RDFS.comment)),
        'subclasses': [str(subclass) for subclass in g.subjects(RDFS.subClassOf, class_uri)],
        'superclasses': [str(superclass) for superclass in g.objects(class_uri, RDFS.subClassOf)],
    }
    return JsonResponse(details)

def property_details(request):
    property_uri = request.GET.get('property_uri')
    g = Graph()
    g.parse(data=request.session['ontology'], format='nt')
    property_uri = URIRef(unquote(property_uri))
    details = {
        'label': str(g.value(property_uri, RDFS.label)),
        'comment': str(g.value(property_uri, RDFS.comment)),
        'domain': [str(domain) for domain in g.objects(property_uri, RDFS.domain)],
        'range': [str(range) for range in g.objects(property_uri, RDFS.range)],
    }
    return JsonResponse(details)

def build_tree(graph, classes):
    tree = {}

    def add_to_tree(cls, parent_tree):
        subclasses = list(graph.subjects(RDFS.subClassOf, cls))
        parent_tree[cls] = {}
        for subclass in subclasses:
            add_to_tree(subclass, parent_tree[cls])

    for cls in classes:
        if not list(graph.objects(cls, RDFS.subClassOf)):
            add_to_tree(cls, tree)

    return tree