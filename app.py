from side_service import app as instance


if __name__ == "__main__":
    instance.run(
        instance.config["HOST"],
        instance.config["PORT"],
        debug=instance.config["DEBUG"]
    )
