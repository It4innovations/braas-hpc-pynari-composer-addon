# BRaaS-HPC-PYNARI Composer

A Blender addon for composing and rendering 3D scenes using the PYNARI (Python ANARI) framework through a visual node-based interface.

## Overview

BRaaS-HPC-PYNARI Composer is a powerful Blender addon that provides a visual node editor for creating PYNARI rendering scenes. PYNARI is a Python binding for ANARI (ANalytic Rendering Interface), which enables high-performance, high-quality rendering for scientific visualization and general-purpose graphics.

This addon allows you to:
- **Visually compose** complex 3D scenes using a node-based workflow
- **Generate Python code** automatically from your node tree
- **Render scenes** using various ANARI-compliant rendering backends (Helide, VisRTX, etc.)
- **Import data** from multiple scientific formats (PyVista, CZI, OpenVDB, etc.)
- **Integrate with Blender** cameras and objects
- **Work remotely** via SSH for HPC workflows (requires BRaaS-HPC addon)

## Features

### Visual Node-Based Composition
- Intuitive drag-and-drop node interface
- Real-time code generation from node trees
- Automatic validation of node connections
- Support for both local and remote file paths

### Comprehensive Node Library
- **Output Nodes**: PILImage, BRaaS-HPC integration
- **Cameras**: Perspective, Orthographic, Blender Camera
- **Geometry**: Triangles, Spheres, Cylinders, Cones, Curves, Quads, IsoSurfaces
- **Materials**: Matte, Physically Based
- **Lights**: Directional, Point, Quad
- **Volumes**: Transfer Functions, Color Ramps, Structured/Unstructured Fields
- **Data Import**: PyVista, CZI, SKImage, PIL, SimpleITK, RAW, OpenVDB
- **Utilities**: Script nodes for custom code, Math operations
- **Input Values**: String, Float, Vector, Integer

### Code Generation
- Generates executable PYNARI Python scripts
- Automatic dependency resolution
- Per-node code generation for debugging
- Auto-generation mode with adjustable FPS

## Installation

### Prerequisites
- **Blender 4.5.0 or higher**
- Python 3.x (included with Blender)

### Install the Addon
  
1. **Open Blender** and go to:
   - `Edit` → `Preferences` → `Add-ons`

2. **Click "Install"** button in the top-right corner

3. Select the zip file and install it

5. **Enable the addon** by checking the checkbox next to "Render: BRaaS-HPC-PYNARIComposer"


## How to Use

### Getting Started

1. **Create a new editor area** or change an existing one to **"Node Editor"**

2. **Select "PYNARI Composer"** from the tree type dropdown (default is "Shader Editor")

3. **Open the PYNARI panel** on the right sidebar (press `N` if not visible)

### Basic Workflow

#### 1. Set Up the Core Structure

Every PYNARI scene requires these essential nodes:

- **Output Node** (PILImage or BRaaS-HPC) - Defines the rendering device and output
- **Frame Node** - Contains the scene setup (camera, world, renderer, resolution)
- **Camera Node** - Defines the viewpoint
- **Renderer Node** - Configures the rendering engine
- **World Node** - Contains all scene objects

**Example basic setup:**
```
[Camera] ──→ [Frame] ──→ [PILImage Output]
[Renderer] ──→ [Frame]
[World] ──→ [Frame]
```

#### 2. Add Scene Content

Inside the **World** node, connect:

- **Group Nodes** - Organize multiple objects
- **Instance Nodes** - Place geometry in the scene
- **Surface Nodes** - Combine geometry with materials
- **Light Nodes** - Add lighting

**Example with geometry:**
```
[Sphere Geometry] ──→ [Matte Material] ──→ [Surface] ──→ [Instance] ──→ [Group] ──→ [World]
                                                                           ↑
                                                    [Point Light] ─────────┘
```

#### 3. Configure Node Properties

- **Select a node** by clicking on it
- **Adjust properties** in the node's panel (appears on left when selected)
- Properties include positions, colors, file paths, and rendering parameters

#### 4. Generate Code

Two ways to generate code:

**Option A - Full Tree Generation:**
1. Click **"Generate Code Tree"** in the PYNARI panel
2. Generates complete executable script
3. Code appears in Blender's Text Editor

**Option B - Single Node Generation (Auto-generate):**
1. Enable **"Auto Generate Node Code"** in the PYNARI panel
2. Set **FPS** for update frequency (1-30 fps)
3. Select any node - its code updates automatically
4. Useful for debugging individual nodes

#### 5. Run or Export

Generated code can be:
- **Copied** from Blender's Text Editor
- **Saved** to a `.py` file
- **Executed** directly with Python + PYNARI installed
- **Submitted** to HPC systems via BRaaS-HPC addon

### Example: Simple Sphere Scene

1. **Add nodes** in this order:
   - Add → Output → PILImage
   - Add → Frame → Frame
   - Add → Cameras → Perspective Camera
   - Add → Render → Renderer
   - Add → Scene → World
   - Add → Scene → Group
   - Add → Scene → Instance
   - Add → Scene → Surface
   - Add → Geometry → Sphere Geometry
   - Add → Materials → Matte Material

2. **Connect nodes:**
   ```
   [Perspective Camera] ──→ Frame.Camera
   [Renderer] ──→ Frame.Renderer
   [World] ──→ Frame.World
   [Frame] ──→ PILImage.Frame
   
   [Sphere Geometry] ──→ Surface.Geometry
   [Matte Material] ──→ Surface.Material
   [Surface] ──→ Instance.Surface
   [Instance] ──→ Group.Instance
   [Group] ──→ World.Instance
   ```

3. **Configure output:**
   - Select PILImage node
   - Set library: `helide` (or your ANARI library)
   - Set device: `default`
   - Set output path and filename: `output.png`

4. **Generate and run:**
   - Click "Generate Code Tree"
   - Copy the generated Python code
   - Run externally with: `python generated_code.py`

## GUI Description

### Main Interface Components

#### 1. Node Editor Area
- **Central workspace** for creating and connecting nodes
- **Add menu** (`Shift + A`) - Browse all available node types
- **Node categories** - Organized by function (Output, Camera, Geometry, etc.)
- **Connection system** - Click and drag between sockets to create links
- **Selection** - Click nodes to select, `A` to select all, `Alt + A` to deselect

#### 2. PYNARI Composer Panel (Right Sidebar)
Located in the Node Editor sidebar (press `N` to toggle):

**Buttons:**
- **Generate Code Tree** - Creates complete Python script from entire node tree
- **Generate Code Node** - Creates code for selected node only

**Auto-generation Settings:**
- **Auto Generate Node Code FPS** - Slider (1-30) sets update frequency
- **Auto Generate Node Code** - Checkbox to enable/disable auto-generation
- **Active Node Display** - Shows currently selected node name

#### 3. Node Properties
When a node is selected:
- **Left panel** shows node-specific properties
- **Input sockets** (left side of node) - Receive data from other nodes
- **Output sockets** (right side of node) - Send data to other nodes
- **Property fields** - Adjust when sockets are not connected

#### 4. Remote Panel (Optional)
Appears when "Enable Remote Access" is enabled in preferences:
- **Remote Path** - Browse remote filesystems
- **File List** - Navigate remote directories
- Requires BRaaS-HPC addon for SSH connectivity

### Node Socket Types (Color-Coded)

- **Frame** - Purple
- **Camera** - Blue
- **Renderer** - Orange
- **World** - Green
- **Group** - Yellow
- **Instance** - Cyan
- **Surface** - Pink
- **Geometry** - Red
- **Material** - Brown
- **Light** - White
- **Volume** - Gray
- **Spatial Field** - Dark Blue
- **Sampler** - Light Green
- **Numpy Array** - Magenta
- **Object** - Olive

Connections are only valid between matching socket types.

### Keyboard Shortcuts

Standard Blender node editor shortcuts apply:
- `Shift + A` - Add node menu
- `X` or `Delete` - Delete selected nodes
- `G` - Move selected nodes
- `Ctrl + C` / `Ctrl + V` - Copy/Paste nodes
- `D` - Duplicate selected nodes
- `Ctrl + Right Click + Drag` - Cut connections
- `F` - Create link between selected nodes

## Advanced Features

### Working with Data Files

The addon supports importing various scientific data formats:

- **PyVista** - Mesh and volume data (.vtu, .vti, etc.)
- **CZI** - Zeiss microscopy images
- **OpenVDB** - Sparse volume data
- **RAW** - Raw binary volume data
- **SimpleITK** - Medical imaging formats
- **PIL** - Standard image formats
- **SKImage** - Scientific imaging data

Use the appropriate "Read" nodes from the **Read Input** category.

### Script Nodes

**Object Script Node** and **Numpy Array Script Node** allow custom Python code:
- Define custom transformations
- Implement complex data processing
- Extend functionality beyond built-in nodes

### Remote Rendering (BRaaS-HPC Integration)

For HPC workflows:
1. **Enable Remote Access** in addon preferences
2. **Install BRaaS-HPC addon** (separate addon)
3. **Use BRaaS-HPC Output node** instead of PILImage
4. **Submit jobs** to supercomputing clusters

### Math and Utility Nodes

- **Math Operations** - Integer, Float, Vector math
- **Dimension to Spacing** - Convert dimensions to spacing for volume data
- **Find Min/Max** - Analyze data ranges

# License
This software is licensed under the terms of the [GNU General Public License](https://github.com/It4innovations/braas-hpc/blob/main/LICENSE).


# Acknowledgement
This work was supported by the Ministry of Education, Youth and Sports of the Czech Republic through the e-INFRA CZ (ID:90254).