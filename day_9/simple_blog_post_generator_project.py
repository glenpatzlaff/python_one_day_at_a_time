blog_post_template = """
# {title}

{body}

---

{footer}
"""

title = input("Enter the blog post title: ")
body = input("Enter the blog post body: ")
footer = input("Enter the footer text: ")

formatted_blog_post = blog_post_template.format(title=title, body=body, footer=footer)

title = title.title()  # Capitalize each word in the title
footer = footer.center(80, '-')  # Center the footer and pad with dashes

formatted_blog_post = blog_post_template.format(title=title, body=body, footer=footer)

print(formatted_blog_post)
