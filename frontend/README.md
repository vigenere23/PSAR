# PSAR - Interface

![interface](https://user-images.githubusercontent.com/32545895/79995525-559b9d80-8485-11ea-8eb5-da559d9e587b.png)

## Project setup

```
yarn install
```

### Compiles and hot-reloads for development

```
yarn serve
```

### Compiles and minifies for production

```
yarn build
```

### Lints and fixes files

```
yarn lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## Helpful informations

**PLEASE** have a look at the [wiki](../wiki/README.md), it is quite usefull!

### Structure

- **`api`** : Contains one file per section that connects to the base station (probably by socket connection)
- **`assets`** : Contains static files like styles and images
- **`components`** : Where all components go. A small hierarchy could be helpful (for grouping bigger sections or component types)
- **`router`** : Only contains the routing file `index.js`. You need to declare all the views in this file. 
- **`views`** : Contains all the views, aka "pages" of the app. Should be helpful for switching between different layers or interfaces (like debug-mode).

### Aliases

For easier importing, there are 2 aliases that has been setup on webpack. 

- **`@`** : Alias for the `src` folder (root). 
- **`styles`** : Alias for the `src/assets/scss` folder. Used for importing inside a `<style>` tag. (**NOTE**: a `~` is needed at the beginning of the path inside the `<style>` tag).

### Pages

- **`/`** : Home page. Will be the main interface.
- **`/widgets`** : Small page to view all the components in action. Helpfull for rapidly debugging component's styling and behavior, without having to play with the layout. 
