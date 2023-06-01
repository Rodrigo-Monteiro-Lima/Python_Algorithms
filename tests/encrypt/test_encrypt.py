from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("rodrigo", 3) == "dor_ogir"
    assert encrypt_message("rodrigo", 4) == "ogi_rdor"
    assert encrypt_message("rodrigo", 10) == "ogirdor"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("rodrigo", "3")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 3)
