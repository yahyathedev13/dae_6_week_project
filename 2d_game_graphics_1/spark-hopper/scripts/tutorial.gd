extends Area2D

var tutorial_anim

func _ready() -> void:
	
	tutorial_anim = get_node("/root/main_game_UI/UI_anim")
	

func _on_body_entered(body: Node2D) -> void:
	if body.name == "player":
		tutorial_anim.play("tutorial")


func _on_body_exited(body: Node2D) -> void:
	if body.name == "player":
		tutorial_anim.play("tutorial finished")
