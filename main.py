# from pyhtml import html, body, h1, p, div, img, a

# template = html(
#     body(
#         h1("Hello, World!"),
#         p("This is a paragraph."),
#         div(
#             img(src="./profile.png", alt="Profile Pic"),
#             a("Click here", href="https://www.google.com")  # Add content inside <a>
#         )
#     )
# )

# print(template.render())

from pyhtml import html, body, a

template = html(
    body(
        a("Click here", href="https://www.google.com")
    )
)

print(template.render())
