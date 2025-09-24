def define_env(env):
    """Mapping d'aliases "façon GTN" vers Font Awesome 6."""
    ALIASES = {
        "gx-eye":              "fa-solid fa-eye",
        "gx-pencil":           "fa-solid fa-pencil",
        "gx-delete":           "fa-solid fa-trash",
        "gx-edit":             "fa-solid fa-pen-to-square",
        "gx-upload":           "fa-solid fa-upload",
        "gx-download":         "fa-solid fa-download",
        "gx-tool":             "fa-solid fa-wrench",
        "gx-tool-version":     "fa-solid fa-cubes",
        "gx-dropdown":         "fa-solid fa-caret-down",
        "gx-param-file":       "fa-regular fa-file",
        "gx-param-files":      "fa-regular fa-copy",
        "gx-param-collection": "fa-regular fa-folder",
        "gx-history-input":    "fa-solid fa-right-to-bracket",
        "gx-param-checkbox":   "fa-regular fa-square-check",
        "gx-param-toggle-off": "fa-solid fa-toggle-off",
        "gx-param-toggle-on":  "fa-solid fa-toggle-on",
        "gx-refresh-history":  "fa-solid fa-arrows-rotate",
        "gx-new-history":      "fa-solid fa-plus",
        "sliders":             "fa-solid fa-sliders",
        "keyboard":            "fa-regular fa-keyboard",
        "laptop":              "fa-solid fa-laptop",
        "hand-pointer":        "fa-solid fa-hand-pointer",
        "font":                "fa-solid fa-font",
        "workflow":            "fa-solid fa-diagram-project",
        "history":             "fa-regular fa-clock",
        "dataset":             "fa-solid fa-database",
        "warning":             "fa-solid fa-triangle-exclamation",
        "info":                "fa-solid fa-circle-info",
        "thumbs-up":           "fa-solid fa-thumbs-up"
    }

    # tailles pratiques → classes FA
    SIZES = {
        "xs": "fa-xs",
        "sm": "fa-sm",
        "1x": "",
        "lg": "fa-lg",
        "2x": "fa-2x",
        "3x": "fa-3x",
    }

    @env.macro
    def icon(name, size="1x", label=None, extra_class="icon", title=None):
        """
        {{ icon('gx-eye') }}
        {{ icon('workflow', size='lg', label='Workflow') }}
        """
        fa = ALIASES.get(name, name)  # permet aussi d'appeler directement une classe FA
        sz = SIZES.get(size, "")
        aria = f' aria-label="{label}"' if label else ' aria-hidden="true"'
        ttl = f' title="{title or label}"' if (title or label) else ""
        cls = " ".join(x for x in [fa, sz, extra_class] if x)
        return f'<i class="{cls}"{aria}{ttl}></i>'
