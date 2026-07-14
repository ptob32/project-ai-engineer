from dataclasses import dataclass

@dataclass
class ApplicationConfig:
    name: str
    version: str


@dataclass
class ServerConfig:
    host: str
    port: int


@dataclass
class EnvironmentConfig:
    database_url: str


@dataclass
class Config:
    application: ApplicationConfig
    server: ServerConfig
    environment: EnvironmentConfig

config_dict = {"application": 
               {"name": "Enterprise AI Platform",
                "version": 0.1}, 

                "logging": {"level": "INFO",
                "log_file": "logs/app.log"},

                "paths": {"data": "data",
                "output": "output"}}