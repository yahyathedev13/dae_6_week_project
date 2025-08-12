extends Area2D

var UI_anim

func _ready() -> void:
	UI_anim = get_node("/root/main_game_UI/UI_anim")



func _on_body_entered(body: Node2D) -> void:
	if body.name == "player":
		UI_anim.play("dash_tutorial")
	

func _on_body_exited(body: Node2D) -> void:
	if body.name == "player":
		UI_anim.play("dash_tutorial_finish")
