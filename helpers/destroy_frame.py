# class DestroyFrame:
def destroyFrame(form):
    # clear the window so you can render new widgets
    if len(form.winfo_children()) > 0:
        for widget in form.winfo_children():
            widget.destroy()