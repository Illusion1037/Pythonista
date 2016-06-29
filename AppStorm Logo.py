import canvas
w = h = 512
canvas.set_size(w, h)
canvas.move_to(w*0.45, h*0.1)
canvas.add_line(w*0.8, h*0.55)
canvas.add_line(w*0.55, h*0.65)
canvas.add_line(w*0.65, h*0.85)
canvas.add_line(w*0.3, h*0.55)
canvas.add_line(w*0.55, h*0.45)
canvas.close_path()
canvas.set_line_width(3)
canvas.draw_path()
canvas.fill_path()
