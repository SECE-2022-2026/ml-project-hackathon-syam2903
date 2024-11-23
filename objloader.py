import os

class Wavefront:
    def __init__(self, obj_path, collect_faces=False):
        self.obj_path = obj_path
        self.vertices = []
        self.faces = []
        self.materials = []
        self.collect_faces = collect_faces
        self.load_obj()

    def load_obj(self):
        if not os.path.exists(self.obj_path):
            raise FileNotFoundError(f"Object file not found: {self.obj_path}")

        with open(self.obj_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            parts = line.split()

            if len(parts) == 0:
                continue

            # Parse vertices (v x y z)
            if parts[0] == 'v':
                vertex = [float(i) for i in parts[1:4]]
                self.vertices.append(vertex)

            # Parse faces (f v1 v2 v3)
            elif parts[0] == 'f' and self.collect_faces:
                face = [int(i.split('/')[0]) - 1 for i in parts[1:4]]  # Obj indices are 1-based, convert to 0-based
                self.faces.append(face)

            # Parse materials (usemtl material_name)
            elif parts[0] == 'usemtl':
                self.materials.append(parts[1])

    def get_faces(self):
        if not self.collect_faces:
            raise ValueError("Faces were not collected, enable collect_faces=True.")
        return self.faces

    def get_vertices(self):
        return self.vertices

    def get_materials(self):
        return self.materials
