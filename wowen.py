import tkinter as tk

# Screen settings
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = "#000000"
WHITE = "#FFFFFF"
GREEN = "#91FF6A"

# Text content
title_text = "WOWEN"
subtitle_text = "Weaving the Web"
description_text = [
    "Expertise in full-stack development, femtech, publishing,",
    "UX, design, and marketing. We transform high-level",
    "strategy into practical implementation, at the intersection",
    "of business development, communication, and technology.",
]
link_text = "Visit us: www.wowen.tech"

# Animation settings
ANIMATION_SPEED = 20  # milliseconds between updates
TEXT_SPEED = 50       # speed of typewriter effect (ms per character)

def animate_title():
    """Animate the title by moving it up and down."""
    global title_direction, title_y
    title_y += title_direction
    if title_y <= 90 or title_y >= 110:
        title_direction *= -1
    canvas.coords(title, WIDTH // 2, title_y)
    root.after(ANIMATION_SPEED, animate_title)

def typewriter_effect(text, x, y, font, fill, line_index=0, char_index=0, objects=None):
    """Display text with a typewriter effect."""
    if objects is None:
        objects = []  # Store references to text objects

    if line_index < len(text):
        # Get the current line and slice up to the current character
        line = text[line_index]
        displayed_text = line[:char_index + 1]

        # If the text object for this line doesn't exist, create it
        if len(objects) <= line_index:
            obj = canvas.create_text(x, y + (line_index * 30), text=displayed_text, font=font, fill=fill, anchor="center")
            objects.append(obj)
        else:
            # Update the existing text object
            canvas.itemconfig(objects[line_index], text=displayed_text)

        # Continue typing the current line
        if char_index < len(line) - 1:
            root.after(TEXT_SPEED, typewriter_effect, text, x, y, font, fill, line_index, char_index + 1, objects)
        else:
            # Move to the next line
            root.after(TEXT_SPEED, typewriter_effect, text, x, y, font, fill, line_index + 1, 0, objects)

# Create the main window
root = tk.Tk()
root.title("WOWEN - Weaving the Web")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg=BLACK)

# Create a canvas to draw text
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BLACK, highlightthickness=0)
canvas.pack()

# Add the title
title_y = 100
title_direction = 1
title = canvas.create_text(WIDTH // 2, title_y, text=title_text, font=("Arial", 36, "bold"), fill=GREEN)

# Add the subtitle
subtitle = canvas.create_text(
    WIDTH // 2, 150, text=subtitle_text, font=("Arial", 24, "italic"), fill=GREEN
)

# Add the description text with typewriter effect
typewriter_effect(description_text, WIDTH // 2, 200, ("Arial", 14), WHITE)

# Add the link
canvas.create_text(
    WIDTH // 2, HEIGHT - 50, text=link_text, font=("Arial", 16), fill=GREEN
)

# Start the title animation
animate_title()

# Run the main loop
root.mainloop()
