extends CanvasLayer




func _on_redo_button_button_up() -> void:
	get_tree().reload_current_scene()
	
