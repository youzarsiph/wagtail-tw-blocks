# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd wagtail_blocks/ui/static/ui
```

To generate the styles:

```console
npm install
npx @tailwindcss/cli -i ../static/ui/css/app.css -o ../static/ui/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
