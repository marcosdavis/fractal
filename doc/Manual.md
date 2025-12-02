# Fractal Visualizer User Manual

*   To begin using the Fractal Visualizer, open the command line and follow the following command format:
    * ```bash
            python src/main.py [FRACTAL_FILE|default [PALETTE_NAME]]
      ``` 
    *   There are 4 supported fractal/fractal file types:
        *   `Mandelbrot`, supported files are:
            *   `m-8-points.frac` 
            *   `m-branches@0064.frac`
            *   `m-branches@0128.frac`
            *   `m-branches@0256.frac`
            *   `m-branches@0512.frac`
            *   `m-branches@1024.frac`
            *   `m-coral.frac`
            *   `m-elephants.frac`
            *   `m-enhance.frac`
            *   `m-leaf.frac`
            *   `m-minibrot.frac`
            *   `m-rabbit-hole.frac`
            *   `m-seahorse.frac`
            *   `m-spiral0.frac`
            *   `m-spiral1.frac`
            *   `m-spiral1@0256.frac`
            *   `m-spiral1@0512.frac`
            *   `m-spiral1@1024.frac`
            *   `m-spiral-jetty.frac`
            *   `m-starfish.frac`
            *   `m-wholly-squid.frac`
            *   `mandelbrot.frac`
            *   `mandelbrot-zoomed.frac`
        *   `Phoenix`, supported files are:
            *   `p-feathers.frac`
            *   `p-monkey-knife-fight.frac`
            *   `p-obconical-kale.frac`
            *   `p-oriental-dragons.frac`
            *   `p-shrimp-cocktail.frac`
            *   `p-tentacles.frac`
            *   `phoenix.frac`  
        *   `Septagon`, supported files are:
            *   `se-mariposa.frac`
            *   `septagon.frac`
        *   `Lambda`, supported files are:
            *   `lambda.frac`
    *   The palette is optional for the program. If you want to see a different color palette, the following are the compatible palette names:
        *   `Toxic`
        *   `OceanLava`
        *   `Joker`
        *   `Moth`
    *   When `default` is put in the place of the fractal file, the program will use the `default` fractal file that it has saved. You can put a palette name after to change the color, or leave it blank to use the `default` palette.
    *   When the `default` fractal and palette is used, the following will be printed:
        *   ```bash
            python src/main.py
            fractal_factory: creating default fractal
            palette_factory: creating default color palette
            Rendering default fractal
            [100% =================================]
            Done in 7.766 seconds!
            Saved image to file default.png
            Close the image window to exit the program
            ``` 
        *   The image will look like the following:[default.png](/default.png) 
        *   Note that `fractal_factory: creating default fractal` and `palette_factory: creating default color palette` were printed. These are printed when ever the default options are used.
    *   Common errors:
        *   If a fractal file that is not compatible is used, an error message will be displayed, similar to the following:
            *    ```bash
                 FileNotFoundError: [Errno 2] No such file or directory: 'data/dragon'
                 ```
            *    Remember to use one of the compatible fractals/fractal files stated above!
        *   If a non-compatible palette is used, an error message will be displayed saying that it is not compatible:
            *   ```bash
                NotImplementedError: batman is not a supported palette
                ``` 
            *   Remember to use one of the compatible palettes that were stated above!
