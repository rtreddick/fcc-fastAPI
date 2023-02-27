---
layout: default
title: Building these Docs
nav_order: 4
description: "Building the docs using Jeckyll, GitHub pages, and just-the-docs"
permalink: /building_these_docs
---

# Building These Docs
{: .fs-9}

An opportunity to learn about Jekyll sites, GitHub pages, and project documentation.
{: .fs-6 .fw-300 }

---

Of course one of the great features of FastAPI is that it automatically builds Swagger docs describing your API. This docs website was not created to duplicate effort, but rather to document the tutorial work itself and highlight some of the things I learned. Building these docs was an amazing learning experience in itself.

## Why go through the effort?

I know it's just a tutorial! But my thought process here is that I need to start producing some collateral to showcase all of the time I put into learning new things and building new skills, even if I'm not producing original content. Prior to building this website, I had never deployed a site to GitHub pages, nor heard of Jekyll. I spent most of one weekend learning about Ruby Gemfiles, Jeckyll, and Liquid templating, researching Jekyll templates, learning more about Github Actions for deployment, and finally getting this website deployed using my custome domain name! Now I have a pattern that I can use to showcase other work, and I understand the foundations of building and deploying static websites to GitHub pages. The work I did here is the scaffold I need to build out a more full-fledged personal website and portfolio (that I can hopefully fill with more exciting original work).

{: .highlight }
I plan to document the work I did to configure this template in just a little more detail. I think my experience might be able to help others who want to learn how to create websites using Jekyll and GitHub pages.

## Just the Docs Template

The template I ended up using is the [Just the Docs](https://github.com/just-the-docs/just-the-docs) template. It's beautiful, functional, and highly configurable. However, one of the challenges I ran into was figuring out how to deploy this site from my docs folder inside the project repo. By default, the template repository is configured to build and deploy from the root directory of your repo. I didn't want to create a separate repository just for my docs. Relocating all the site files to the docs folder and updating the GitHub Actions workflow appropriately created a surprising amount of pain. I got a good hint from the project maintainer by starting a [discussion](https://github.com/just-the-docs/just-the-docs/discussions/1183) in their repo, and with a little more poking around and reading the docs for the particular actions being used, I finally figured it out! Hopefully, the discussion I started helps others who have the same use case.

{: .note }
I used the gem-based, template approach which was recommended in the [Getting Started](https://just-the-docs.github.io/just-the-docs/#getting-started) section of the Just the Docs homepage. After scanning the docs a little more, it seems I probably could have used Just The Docs as a remote theme as supported by Github. Since GitHub uses Jekyll as its default static site generator behind the scenes, maybe that approach would simplfy things. I will research that for future projects. For now, I've got a working site!