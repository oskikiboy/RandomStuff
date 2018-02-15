# RandomStuff written by Oscar (https://oskikiboy.me) and StackOverflow stuff.

# Imports.
import os
from time import sleep
from pluginbase import PluginBase

# Gather plugins.
plugin_base = PluginBase(package="main.plugins")
plugin_source = plugin_base.make_plugin_source(
    searchpath=["./plugins"]
    )

# To clear screen.
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Load a plugin.
def loadPL(a):
    cls()
    a = int(a)
    a -= 1
    fromArray = plugin_source.list_plugins()[a]
    SelectedPlugin = plugin_source.load_plugin(fromArray)
    SelectedPlugin.run()

# Main method.
def main():
    # Display plugin list.
    num = 1
    cls()
    print("Plugins list:")
    for x in plugin_source.list_plugins():
        print(f"Plugin {num}: {x}")
        num += 1
    print("To exit, type \"exit\"")
    a = input("What plugin would you like to run? ")

    # Verify the input.
    if a == "exit":
        cls()
        print("Thanks for playing!")
        exit()
    elif not a.isdigit():
        numPL = 1
        a = a.lowe
        if a in plugin_source.list_plugins():
            for b in plugin_source.list_plugins():
                if a == b:
                    # Load the plugin if it is a valid name.
                    loadPL(numPL)
                else:
                    numPL += 1
        else:
            cls()
            print("Please enter a number or valid plugin name!\nResuming in two seconds.")
            sleep(2)
            main()
    elif int(a) > len(plugin_source.list_plugins()) or int(a) == 0:
        cls()
        print("Please enter a valid number!\nResuming in two seconds.")
        sleep(2)
        main()
    else:
        # Load the plugin if the conditions pass.
        loadPL(a)

# Run the program.
main()
