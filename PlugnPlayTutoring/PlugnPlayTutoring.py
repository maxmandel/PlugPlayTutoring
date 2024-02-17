import reflex as rx

class State(rx.State):
    pass

def index():
    return rx.vstack(
        # Title at the top, centered
        rx.heading("Plug and Play Tutoring", font_size="2em", alignment="center"),
        
        # Menu buttons on the left-hand side
        rx.vstack(
            rx.button("About Us", color_scheme="blue", font_size="1.2em", alignment="left"),
            rx.button("Calendar", color_scheme="blue", font_size="1.2em", alignment="left"),
            rx.button("Tutee Enrollment", color_scheme="blue", font_size="1.2em", alignment="left"),
            rx.button("Tutor Application", color_scheme="blue", font_size="1.2em", alignment="left"),
            spacing="1em",
            alignment="left",
        ),
        
        alignment="center",  # Center everything vertically
        spacing="2em"  # Add some spacing between elements
    )

app = rx.App()
app.add_page(index)
