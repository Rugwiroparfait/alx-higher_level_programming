# 0x15. JavaScript - Web jQuery

## Description

This project focuses on using JavaScript and jQuery to manipulate the DOM, handle events, and perform AJAX requests. It is part of the SE Foundations curriculum with an average score of 82.52%. The project covers key concepts in JavaScript and jQuery to facilitate dynamic and interactive web development.

## Author

**NSANZIMANA RUGWIRO Dominique Parfait**

## Project Details

- **Start Date:** June 12, 2024, 6:00 AM
- **End Date:** June 13, 2024, 6:00 AM
- **Weight:** 1
- **Manual QA Review:** Required (request it when you are done with the project)

## Concepts

For this project, you should be familiar with the following concepts:

- JavaScript in the browser
- Dealing with data statically versus dynamically

## Resources

Read or watch the following resources to better understand the project requirements and objectives:

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction)
- [Selector](https://learn.jquery.com/using-jquery-core/selecting-elements/)
- [Get and set content](https://learn.jquery.com/using-jquery-core/manipulating-elements/)
- [Manipulate CSS classes](https://api.jquery.com/category/manipulation/class-attribute/)
- [Manipulate DOM elements](https://api.jquery.com/category/manipulation/)
- [API](https://developer.mozilla.org/en-US/docs/Web/API)
- [Introduction](https://api.jquery.com/jQuery.ajax/)
- [GET & POST request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [JQuery](https://jquery.com/)
- [JQuery API](https://api.jquery.com/)
- [JQuery Ajax](https://api.jquery.com/jQuery.ajax/)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without needing to look them up:

### General

- Why jQuery makes front-end programming easier (don't forget to tweet today with the hashtag #ilovejquery :))
- How to select HTML elements in JavaScript
- How to select HTML elements with jQuery
- Differences between ID, class, and tag name selectors
- How to modify an HTML element's style
- How to get and update an HTML element's content
- How to modify the DOM
- How to make a GET request with jQuery Ajax
- How to make a POST request with jQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Chrome (version 57.0)
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant with the flag `--global $: semistandard *.js --global $`
- You must use jQuery version 3.x
- You are not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

### Import jQuery

```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

## Manual QA Review

It is your responsibility to request a review for this project from a peer before the project's deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

## Tasks

### 0. No jQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag
- You can't use the jQuery API

**File:** `0-script.js`

### 1. With jQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API

**File:** `1-script.js`

### 2. Click and turn red

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API

**File:** `2-script.js`

### 3. Add `.red` class

Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`:

- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API

**File:** `3-script.js`

### 4. Toggle classes

Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:

- The `<header>` element must always have one class: `red` or `green`, never both at the same time and never empty.
- If the current class is `red`, when the user clicks on `DIV#toggle_header`, the class must be updated to `green`; and vice versa.
- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API

**File:** `4-script.js`

### 5. List of elements

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API

**File:** `5-script.js`

### 6. Change the text

Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on `DIV#update_header`:

- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API

**File:** `6-script.js`

### 7. Star Wars character

Write a JavaScript script that fetches the character name from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`

- The name must be displayed in the HTML tag `DIV#character`
- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API

**File:** `7-script.js`

### 8. Star Wars movies

Write a JavaScript script that fetches and lists the title for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`

- All movie titles must be listed in the HTML tag `UL#list_movies`
- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API

**File:** `8-script.js`

### 9. Say Hello!

Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.

- The translation of “hello” must be displayed in the HTML tag `DIV#hello`
- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Your script must work when it is imported from the `<head>` tag

**File:** `9-script.js`

## Repository

- **GitHub Repository:** `alx-higher_level_programming`
- **Directory:** `0x15-javascript-web_jquery`

---

**Note:** All tasks should be tested with the corresponding HTML files provided in the project description. Ensure your solutions are semistandard compliant and use jQuery version 3.x.