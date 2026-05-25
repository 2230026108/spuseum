"""
inspect_glb.py  —  列出 museumvr.glb 里所有 mesh 名称
需要: pip install pygltflib
"""
import json, sys

try:
    from pygltflib import GLTF2
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygltflib", "-q"])
    from pygltflib import GLTF2

glb_path = r"c:\Users\19741\WorkBuddy\20260523165257\Spuseum-main\public\models\airplane\museumvr.glb"

glb = GLTF2().load(glb_path)

print("=== 所有 mesh 名称 ===")
for i, mesh in enumerate(glb.meshes):
    print(f"  mesh[{i:03d}]  name={repr(mesh.name)}")

print("\n=== 所有 node 名称（含父子关系） ===")
for i, node in enumerate(glb.nodes):
    mesh_idx = node.mesh
    mesh_name = glb.meshes[mesh_idx].name if mesh_idx is not None and mesh_idx < len(glb.meshes) else "-"
    print(f"  node[{i:03d}]  node_name={repr(node.name):40s}  mesh={repr(mesh_name)}")

print(f"\n共 {len(glb.meshes)} 个 mesh, {len(glb.nodes)} 个 node")
