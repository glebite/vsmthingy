import dearpygui.dearpygui as dpg


breakpoint()
# create some items in the window
with dpg.window(label="Animation", width=500, height=500):
    # create three buttons and a progress bar
    button1 = dpg.add_button(label="Button 1")
    # button2 = dpg.add_button(label="Button 2")
    # button3 = dpg.add_button(label="Button 3")
    # progress_bar = dpg.add_progress_bar()

    # # place the buttons side by side using the add_same_line function
    # dpg.add_same_line(spacing=50)
    # dpg.add_text("Animation:")
    # animation_button1 = dpg.add_button(label=" ", width=30)
    # animation_button2 = dpg.add_button(label=" ", width=30)
    # animation_button3 = dpg.add_button(label=" ", width=30)


# define a function that updates the animation buttons and progress bar
def update_animation():
    state1 = " " if dpg.get_item_state(button1) else "X"
    state2 = " " if dpg.get_item_state(button2) else "X"
    state3 = " " if dpg.get_item_state(button3) else "X"
    dpg.configure_item(animation_button1, label=state1)
    dpg.configure_item(animation_button2, label=state2)
    dpg.configure_item(animation_button3, label=state3)

    progress = 0
    if dpg.get_item_state(button1):
        progress = 33
    elif dpg.get_item_state(button2):
        progress = 66
    elif dpg.get_item_state(button3):
        progress = 100
    dpg.configure_item(progress_bar, value=progress)


# create a timer that updates the animation every 100 milliseconds
with dpg.timer(0.1, callback=update_animation, user_data=None):
    pass

dpg.show_viewport()
# start the Dear PyGui event loop
dpg.start_dearpygui()
