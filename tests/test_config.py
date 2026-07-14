from enterprise_ai_platform.config import load_config


def test_load_config():
    config = load_config()

    assert config["application"]["name"] == "Enterprise AI Platform"
    assert config["logging"]["level"] == "INFO"