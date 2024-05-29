# pelican-blog
## Installation
- Install Pelican and Markdown.

``` bash
python -m pip install "pelican[markdown]"
```

## Create an article
- Create your first article with the following content in `./content/keyboard-review.md`:

``` md
Title: My First Review
Date: 2010-12-03 10:20
Category: Review

Following is a review of my favorite mechanical keyboard.
```

## Preview
- Preview your site by navigating to http://localhost:8000/ in your browser.

``` bash
pelican -r -l
```

## Deployment

```
pelican content
```