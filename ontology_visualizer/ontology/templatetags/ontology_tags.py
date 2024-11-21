from django import template

register = template.Library()

@register.inclusion_tag('ontology/tree_node.html')
def render_tree(tree):
    return {'tree': tree}