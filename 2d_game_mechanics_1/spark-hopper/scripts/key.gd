extends Area2D


func _on_body_entered(body: Node2D) -> void:
	
	if body.name == "player":
		get_node("/root/main_game_UI/UI_anim").play("key_obtained")
		queue_free()
		body.has_key = true

		
