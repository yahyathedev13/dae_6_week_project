extends CanvasLayer




func _on_redo_button_button_up() -> void:
	get_tree().reload_current_scene()
	


func _on_pause_pressed() -> void:
	
	get_tree().paused = true
	$pause_menu.visible = true



func _on_unpause_pressed() -> void:
	get_tree().paused = false
	$pause_menu.visible = false


func _on_restart_pressed() -> void:
	get_tree().reload_current_scene()
	$pause_menu.visible = false
	get_tree().paused = false
