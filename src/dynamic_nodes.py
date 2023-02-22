import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


def link_callback(sender, app_data):
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)


def delink_callback(sender, app_data):
    dpg.delete_item(app_data)


def node():
    with dpg.node(label="Step", parent="node_editor"):
        dpg.add_node_attribute(label="Type", attribute_type=dpg.mvNode_Attr_Input)
        dpg.add_node_attribute(label="Category", attribute_type=dpg.mvNode_Attr_Input)
        dpg.add_node_attribute(label="output", attribute_type=dpg.mvNode_Attr_Output)


def delete():
    for node in dpg.get_selected_nodes("node_editor"):
        dpg.delete_item(node)


with dpg.window(width=1000, height=700):
    dpg.add_node_editor(tag="node_editor", callback=link_callback,
                        delink_callback=delink_callback)


with dpg.window(pos=[1100, 100]):
    dpg.add_button(label="Create Node", callback=node)
    dpg.add_button(label="Delete Nodes", callback=delete)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
