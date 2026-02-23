import os
from huggingface_hub import HfApi

REPO_ID = os.environ["HF_REPO_ID"]          # e.g. Oddsflowai-team/agent-reputation-network
REPO_TYPE = os.environ.get("HF_REPO_TYPE", "model")
TOKEN = os.environ["HF_TOKEN"]

api = HfApi(token=TOKEN)

api.upload_folder(
    repo_id=REPO_ID,
    repo_type=REPO_TYPE,
    folder_path=".",
    ignore_patterns=[
        ".git/**",
        ".github/**",          # ✅ 不上传工作流文件
        "**/__pycache__/**",
        "**/*.pyc",
    ],
)

print("✅ Uploaded to HF:", REPO_ID)
