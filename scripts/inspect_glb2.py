"""
inspect_glb2.py  — 专门列出所有和 Art_Work 相关的 node 名称
"""
try:
    from pygltflib import GLTF2
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygltflib", "-q"])
    from pygltflib import GLTF2

glb_path = r"c:\Users\19741\WorkBuddy\20260523165257\Spuseum-main\public\models\airplane\museumvr.glb"
glb = GLTF2().load(glb_path)

print("=== Art_Work 相关的 mesh 名 ===")
art_meshes = []
for i, mesh in enumerate(glb.meshes):
    if mesh.name and "art_work" in mesh.name.lower():
        art_meshes.append((i, mesh.name))
        print(f"  mesh[{i:03d}]  {repr(mesh.name)}")

print(f"\n共找到 {len(art_meshes)} 个 Art_Work mesh\n")

print("=== Art_Work 相关的 node 名 ===")
art_nodes = []
for i, node in enumerate(glb.nodes):
    if node.name and "art_work" in node.name.lower():
        mesh_name = glb.meshes[node.mesh].name if node.mesh is not None else "NO_MESH"
        art_nodes.append((i, node.name, mesh_name))
        print(f"  node[{i:03d}]  node={repr(node.name):50s}  mesh={repr(mesh_name)}")

print(f"\n共找到 {len(art_nodes)} 个 Art_Work node\n")

# 只看画布（非 Frame）的
print("=== 非 Frame 的 Art_Work node ===")
for i, nname, mname in art_nodes:
    if "frame" not in nname.lower():
        print(f"  node[{i:03d}]  {repr(nname)}")
