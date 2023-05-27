# Tiny Tapeout 03p5

* Visit https://tinytapeout.com for more information on the project and how to get involved.

This is a prototype Tiny Tapeout using the new Mux.

## Configure

```
export PDK_ROOT=<some dir>/pdk
export OPENLANE_ROOT=<some dir>/openlane
make setup
git clone https://github.com/TinyTapeout/tt-multiplexer/
pip install -r tt-multiplexer/proto/requirements.txt
make gen-user-module
```

Then apply a patch to `tt-multiplexer/proto/tt_mux.v`, which sets the number of columns per mux to 8,
and works around an issue with `yosys` inserting buffers on the `spine_ow` signals, after the tristate buffers output.

```
git apply --directory=tt-multiplexer tt_mux.patch
```

Important: make sure you are using efabless/openlane docker tag 2023.05.19 (or newer). 
Previous version may introduce a bug in the `tt_mux` that will result in disconnected `um_ow` signals.

## Fetch projects

Set `GH_USERNAME` and `GH_TOKEN` environment variables with your GitHub username and a personal access token, respectively.
To generate your GH_TOKEN go to https://github.com/settings/tokens/new . Set the checkboxes for repo and workflow.

Then clone the tt03p5 branch from the tt-support-tools repo and install the required packages:

```
git clone -b tt03p5 https://github.com/tinytapeout/tt-support-tools tt 
```

Finally, run the following commands to fetch the user projects and generate the configuration for the user_project_wrapper:

```
pip install -r tt/requirements.txt
python tt/configure.py --clone-all --fetch-gds --update-caravel
```

## Harden

```
make tt_ctrl
make tt_mux
make tt_um_test
python gen_macro_cfg.py
make user_project_wrapper
```

Note: `user_project_wrapper` currently has LVS errors. It should have exactly 51 errors - otherwise, there's something wrong (probably with the PDN not connecting to macros).
