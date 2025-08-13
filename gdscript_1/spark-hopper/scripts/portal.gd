extends Area2D


func _on_body_entered(body: Node2D) -> void:
	if body.name == "player":
		if body.has_key == true:
			get_tree().change_scene_to_file("res://scenes/level_2.tscn")
			$AnimatedSprite2D.play("open")
		elif body.has_key == false:
			get_node("/root/main_game_UI/UI_anim").play("sorry_no_key")
		
