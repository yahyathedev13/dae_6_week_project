extends CanvasLayer


func _on_button_pressed() -> void:
	
	$AnimationPlayer.play("next_scene_transition")


func _on_animation_player_animation_finished(anim_name: StringName) -> void:
	if anim_name == "next_scene_transition":
		get_tree().change_scene_to_file("res://scenes/test_scene.tscn")
