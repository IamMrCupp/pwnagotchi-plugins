# pwnagotchi-plugins


This repo contains my custom plugins for pwnagotchi devices.
Much of the work has been developed using the jayofelony image for pwnagotchi. This version does not contain the "AI neural network" features that exist in the evilsocket versions.


If you have enjoyed using these plugins, please help me stay caffeinated by donating to my caffeine fund 😁
<a href="https://www.buymeacoffee.com/IamMrCupp" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Yellow button with coffee cup icon and text Buy Me A Coffee on bright yellow background - clickable donation link" style="height: 30px !important;width: 130px !important;" ></a>


#### Repo Layout:
<pre>
.
├── .gitignore
├── .vscode                     
│   └── settings.json           # vscode setting files
├── agev3.py                    # Agev3 plugin
├── docs                        
│   └── images                  
│       └── agev3.png           # Agev3 Screenshot
├── README.md                   
└── stubs                       # These are "stubs" for local python development
    └── pwnagotchi
        ├── __init__.py
        ├── plugins
        │   └── __init__.py
        └── ui
            ├── __init__.py
            ├── components.py
            ├── fonts.py
            └── view.py
</pre>

### Required for plugin use
You will need to ensure that you have configured the `custom_plugins` feature in your TOML config file.
```
    main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"`
```

You have two options for installing and using the plugins:

#### Configure pwnagotchi to use plugins manager feature
- Add the repo
    ``` bash
    # ... 
    main.custom_plugin_repos = [
       "https://github.com/IamMrCupp/pwnagotchi-plugins/archive/master.zip",
    ]
    ```
- update plugins
    ``` bash
    sudo pwnagotchi plugins update
    ```


---

## agev3.py plugin

![screenshot](docs/images/agev3.png)

This is the age plugin that I am using at the moment due to the lack of calculated Age being displayed while using the jayofelony image. The above image shows the Age feature surrounded by the red squiggly rectangle.

### Overview 
The plugin determines the Age of the pwnagotchi by crawling over the filesystem and stating a few files. It uses the information harvested off the file creation date and writes out a json blob to be used as the device Birth Date.

### Use
- install & enabled plugin
    ```
    sudo pwnagotchi plugins install agev3
    sudo pwnagotchi plugins enable agev3
    ``` 

- Enable the plugin by adding the following to your `config.toml`
    ```
    main.plugins.agev3.enabled = true
    main.plugins.agev3.age_x_coord = 0
    main.plugins.agev3.age_y_coord = 80
    ```

- Restart the pwnagotchi app
    ``` bash
    pwnkill
    ```