# ⭐ RasterRenderer2 feature support

## Introduction

`RasterRenderer2` is an introduced in PyGerber 2.2.0 raster backend for rendering of
Gerber files. It replaced legacy `Rasterized2DBackend` which now is deprecated along
with `Parser` class. `RasterRenderer2` operates on command buffers generated by
`Parser2`. It is capable of outputting PNG and JPEG images with official API, although
it is possible to acquire raw Pillow image objects and save them in different formats.

| Symbol | Meaning                                    |
| ------ | ------------------------------------------ |
| ✅     | Feature implemented and usable.            |
| 🚧     | Work in progress. Related APIs can change. |
| 🚫     | Not planned, unless contributed or needed. |
| ❌     | Not implemented, but planned.              |
| 👽     | Partially implemented.                     |
| 👾     | Bugged.                                    |
| ⛔     | Feature doesn't apply.                     |

## Supported Gerber X3 features

### General

-   ✅ LP - Load polarity.
-   ✅ LM - Load mirroring.
-   ✅ LR - Load rotation.
-   ✅ LS - Load scaling.

### D01, D02, D03

-   ✅ D01 - Plot operation, mode
    -   ✅ Line, with:
        -   ✅ circle,
        -   ✅ rectangle,
        -   ✅ obround,
        -   ✅ polygon,
        -   ✅ macro.
    -   ✅ Arc, with:
        -   ✅ circle,
        -   ✅ rectangle,
        -   ✅ obround,
        -   ✅ polygon,
        -   ✅ macro.
    -   ✅ Counter clockwise arc, with:
        -   ✅ circle,
        -   ✅ rectangle,
        -   ✅ obround,
        -   ✅ polygon,
        -   ✅ macro.
-   ✅ D03 - Flash operation, with
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.

### Regions

-   ✅ Regions, with:
    -   ✅ Line,
    -   ✅ Arc,
    -   ✅ Counter clockwise arc.

### Macros

-   ⛔ Parameters.
-   👽 Primitives in definition:
    -   ✅ Code 1, Circle
    -   ❌ Code 2, Vector line
    -   ✅ Code 4, Outline
    -   ✅ Code 5, Polygon
    -   ❌ Code 6, Moire
    -   ✅ Code 7, Thermal
    -   ✅ Code 20, Vector line
    -   ✅ Code 21, Center Line
    -   ❌ Code 22, Lower Left Line
-   👽 Primitives in aperture instance:
    -   ✅ Code 1, Circle
    -   ❌ Code 2, Vector line
    -   ✅ Code 4, Outline
    -   ✅ Code 5, Polygon
    -   ❌ Code 6, Moire
    -   ❌ Code 7, Thermal
    -   ✅ Code 20, Vector line
    -   ✅ Code 21, Center Line
    -   ❌ Code 22, Lower Left Line
-   ❌ Rotation around macro origin:
    -   ❌ Code 1, Circle
    -   ❌ Code 2, Vector line
    -   ❌ Code 4, Outline
    -   ❌ Code 5, Polygon
    -   ❌ Code 6, Moire
    -   ❌ Code 7, Thermal
    -   ❌ Code 20, Vector line
    -   ❌ Code 21, Center Line
    -   ❌ Code 22, Lower Left Line
-   ⛔ Expressions.
    -   ⛔ Constants.
    -   ⛔ Variables.
    -   ⛔ Addition.
    -   ⛔ Subtraction.
    -   ⛔ Multiplication.
    -   ⛔ Division.
    -   ⛔ Unary + operator.
    -   ⛔ Negation.
-   ⛔ Variable definitions.

### Aperture blocks

-   ✅ Nested Line, aperture:
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.
-   ✅ Nested Arc, aperture:
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.
-   ✅ Nested Counter clockwise arc, aperture:
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.
-   ✅ Nested Flash:
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.
-   ✅ Nested regions.

### Step and repeat

-   ✅ Nested Line, aperture:
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.
-   ✅ Nested Arc, aperture:
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.
-   ✅ Nested Counter clockwise arc, aperture:
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.
-   ✅ Nested Flash:
    -   ✅ circle,
    -   ✅ rectangle,
    -   ✅ obround,
    -   ✅ polygon,
    -   ✅ macro.
-   ✅ Nested regions.
-   ✅ Nested blocks.

## Supported DEPRECATED Gerber features

-   ❌ IR - Sets 'Image rotation' graphics state parameter. (Spec. 8.1.5)
-   ❌ MI - Sets 'Image mirroring' graphics state parameter (Spec. 8.1.7)
-   ❌ OF - Sets 'Image offset' graphics state parameter (Spec. 8.1.8)
-   ❌ SF - Sets 'Scale factor' graphics state parameter (Spec. 8.1.9)
-   ✅ G74 - Sets single quadrant mode. (Spec. 8.1.10)
-   🚫 Format Specification (FS) Options. (Spec. 8.2.1)
-   🚫 Rectangular aperture hole in standard apertures. (Spec. 8.2.2)
-   👽 Draws and arcs wit rectangular apertures. (Spec. 8.2.3)
-   ❌ Macro Primitive Code 2, Vector Line. (Spec 8.2.4)
-   ❌ Macro Primitive Code 22, Lower Left Line. (Spec 8.2.5)
-   ❌ Macro Primitive Code 6, Moiré. (Spec 8.2.6)
-   ✅ Combining G01/G02/G03/G70/G71 and D01 in a single command. (Spec 8.3.1)
-   ✅ Combining G01/G02/G03/G70/G71 and D02 in a single command. (Spec 8.3.1)
-   ✅ Combining G01/G02/G03/G70/G71 and D03 in a single command. (Spec 8.3.1)
-   ⛔ Coordinate Data without Operation Code. (Spec 8.3.2)
-   ⛔ Style Variations in Command Codes. (Spec 8.3.3)
-   ❌ Deprecated usage of SR. (Spec 8.3.4)
-   ❌ Deprecated Attribute Values. (Spec 8.4)

    -   **Important**: _Incremental notation itself is not supported and is not planned
        due to lack of test assets and expected complications during implementation._

> PS. I had great time adding emoji to this table.
