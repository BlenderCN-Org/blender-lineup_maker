import bpy

class LM_PT_main(bpy.types.Panel):          
    bl_label = "Lineup Maker"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Lineup Maker'
    
    def draw(self, context):
        scn = context.scene
        assetPath = bpy.path.abspath(scn.lm_asset_path)
        print(assetPath)
        layout = self.layout
        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(scn, 'lm_asset_path', text = 'Asset Path')
        col.prop(scn, 'lm_naming_convention', text = 'Naming Convention')
        col.operator("scene.lm_importfiles", icon='IMPORT', text="Import all assets")

