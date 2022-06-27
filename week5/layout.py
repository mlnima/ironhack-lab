from ipywidgets import AppLayout, Button, Layout

def create_expanded_button(description, button_style):
    return Button(description=description, button_style=button_style, layout=Layout(height='auto', width='auto'))

header_button = create_expanded_button('Header', 'success')
left_button = create_expanded_button('Left', 'info')
center_button = create_expanded_button('Center', 'warning')
right_button = create_expanded_button('Right', 'info')
footer_button = create_expanded_button('Footer', 'success')

appLayout = AppLayout(
    header=header_button,
    left_sidebar=left_button,
    center=center_button,
    right_sidebar=right_button,
    footer=footer_button
)
