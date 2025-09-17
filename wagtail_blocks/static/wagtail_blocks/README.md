# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd .\wagtail_blocks\static\wagtail_blocks\
```

To generate the styles:

```console
npm install
cd .\wagtail_blocks\static\wagtail_blocks\
npx @tailwindcss/cli -i ../static/wagtail_blocks/css/app.css -o ../static/wagtail_blocks/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
