import os
import bpy
import bmesh
from mathutils import Vector
import src.consts as consts


def get_current_path():
    file_path = bpy.data.filepath
    return os.path.dirname(os.path.dirname(file_path))


def create_folder_if_needed(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_aligned_bounding_box(ob):
    bbox_corners = [tuple(ob.matrix_world @ Vector(corner)) for corner in ob.bound_box]
    lower_vert = Vector([ min([v[i] for v in bbox_corners]) for i in range(3) ])
    upper_vert = Vector([ max([v[i] for v in bbox_corners]) for i in range(3) ])
    center = (upper_vert + lower_vert)/2
    scale = upper_vert - lower_vert
    # avoid 2D box
    scale += Vector([1, 1, 1]) * 1e-3
    return (center, scale)





def deep_copy_object(obj):
    copy = obj.copy()
    copy.data = obj.data.copy()
    copy.animation_data_clear()
    if copy.data.shape_keys:
        copy.data.shape_keys.animation_data_clear()
    return copy


# https://sinestesia.co/blog/tutorials/python-rounded-cube/
def apply_modifiers(obj):
    """ Apply all modifiers on an object """

    bm = bmesh.new()
    dg = bpy.context.evaluated_depsgraph_get()
    bm.from_object(obj, dg)
    bm.to_mesh(obj.data)
    bm.free()
    obj.modifiers.clear()


def select_obj(obj):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def import_svg_in_blender_as_collection(svg_filepath):
    # trick to find the objects created for the import:
    collections_pre_import = set([ o.name for o in bpy.data.collections ])
    bpy.ops.import_curve.svg(filepath=svg_filepath)
    collections_post_import = set([ o.name for o in bpy.data.collections ])
    new_collection = collections_post_import.difference(collections_pre_import).pop()
    return new_collection


def create_bpy_collection(name="New Collection", hide_viewport=False, hide_render=False):
        scene_master_col = bpy.context.scene.collection
        new_col = bpy.data.collections.new(name)
        scene_master_col.children.link(new_col)
        new_col.hide_viewport = hide_viewport
        new_col.hide_render = hide_render
        return new_col


def remove_bpy_collection(col):
    scene_master_col = bpy.context.scene.collection
    scene_master_col.children.unlink(col)



def save_blend_file(path):
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(
        consts.CURRENT_PATH,
        path
    ))
