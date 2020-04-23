# Frontend setup: Vuetify

The UI has now been setup with [Vuetify](https://vuetifyjs.com/en/components/api-explorer/). This means you can now easily use its components. It has been installed through [`vue-cli`](https://vuetifyjs.com/en/getting-started/quick-start/#vue-cli-install). The complete configuration includes:

- Vuetify's injection to the app
- Configuration with Vue
- Optimized build time
- SASS variables customization

### SASS variables and style customization

Since Vuetify is a UI kit, it is normally really hard and cumbersome to edit the base style. Hopefully, Vuetify devs were kind enough to code every major styles into SASS variables, and offer a way to overwrite those. That means, most of the time, only redefining some variables will be plenty enough to change the style. Be sure to read carefully each component's `API` section (ex: [button's api](https://vuetifyjs.com/en/components/buttons/#api)). Since the framework will need to recompile every time, you may experience some slower build times when changing these variables. 

To overwrite the variables defined in the `API` section, you juste have to define them in the `src/styles/variables.scss` file.

:warning: **Please make sure that the same variable is not already present**, since you break another components style.

[BACK](./README.md)
