# pwnagotchi-plugins


This repo contains my custom plugins for pwnagotchi devices.
Much of the work has been developed using the jayofelony image for pwnagotchi. This version does not contain the "AI neural network" features that exist in the evilsocket versions.

You will need to ensure that you have configured the `custom_plugins` feature in your TOML config file.
```
main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"`
```

You have two options for installing and using the plugins:

#### Option #1: Configure pwnagotchi to use plugin manager feature
- Add the repo
  ```
    main.custom_plugin_repos = [
       "https://github.com/IamMrCupp/pwnagotchi-plugins/archive/master.zip",
    ]
  ```
- update plugins
  ```
  sudo pwnagotchi plugin update
  ```
- install & enabled plugin
  ```
  sudo pwnagotchi plugin install agev3
  sudo pwnagotchi plugin enable agev3
  ``` 

#### Option #2: Copy the plugin by hand
-  

Repo Layout:
<pre>
.
├── plugins
│   └── agev3.py
└── README.md
</pre>

---
### agev3.py plugin
This is the age plugin that I am using at the moment due to the lack of calculated Age being displayed while using the jayofelony image.

Enable the plugin by adding the following to your `config.toml`
```
main.plugins.agev3.enabled = true
main.plugins.agev3.age_x_coord = 0
main.plugins.agev3.age_y_coord = 80
```