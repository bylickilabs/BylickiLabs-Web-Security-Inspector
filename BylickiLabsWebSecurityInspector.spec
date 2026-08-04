# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

matplotlib_datas, matplotlib_binaries, matplotlib_hidden = collect_all("matplotlib")
scipy_datas, scipy_binaries, scipy_hidden = collect_all("scipy")

analysis = Analysis(
    ["main.py"],
    pathex=[],
    binaries=matplotlib_binaries + scipy_binaries,
    datas=[("assets", "assets")] + matplotlib_datas + scipy_datas,
    hiddenimports=matplotlib_hidden + scipy_hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(analysis.pure)
exe = EXE(
    pyz,
    analysis.scripts,
    [],
    exclude_binaries=True,
    name="BylickiLabsWebSecurityInspector",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="assets/app_icon.ico",
)
collection = COLLECT(
    exe,
    analysis.binaries,
    analysis.datas,
    strip=False,
    upx=True,
    name="BylickiLabsWebSecurityInspector",
)
