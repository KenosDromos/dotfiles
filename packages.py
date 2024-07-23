PACMAN = {
    "BASE" : [
        "base-devel", "make", "cmake", "linux-headers", 
    ],
    "ENVIRONMENTS" : [
        "wayland", "wayland-protocols", "xorg-server-xwayland",
        "qt5-wayland", "qt6-wayland"
    ],
    "ENVIRONMENTS_ADDITION" : [
        # Screenshot
        # "grim", "slurp",
    ],
    "WINDOWS_MANAGER_COMPONENTS" : [
        "hyprland"
    ],
    "NVIDIA_DRIVER" : [
        "nvidia-dkms", "nvidia-utils", "nvidia-settings"
    ]
}
AUR = {

}
