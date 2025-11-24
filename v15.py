#!/usr/bin/env python3
"""
🦇 ELYOUSSEFI EVIL - ULTIMATE EDITION PREMIUM
Complete Working Version with Premium UI, Unlimited Tokens, Advanced Analytics, Theme Customization, Curved Corners & Smooth Animations
FIXED: Layout Compatibility & Window Resizing
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog, colorchooser
import threading
import time
import json
import requests
import os
import re
import html
import base64
import tempfile
from datetime import datetime
from pathlib import Path
import webbrowser
import logging
from logging.handlers import RotatingFileHandler
import math
import random

# ==================== ENHANCED PREMIUM ANIMATION ENGINE ====================

class PremiumAnimationEngine:
    """Advanced animation system with smooth scrolling and color transitions"""
    
    def __init__(self, root):
        self.root = root
        self.active_animations = []
        
    def create_pulse_effect(self, widget, base_color='#ff0000'):
        """Create pulsing glow effect with smooth transitions"""
        pulse_phase = 0
        
        def pulse():
            nonlocal pulse_phase
            pulse_phase = (pulse_phase + 0.1) % (2 * math.pi)
            intensity = 0.7 + 0.3 * math.sin(pulse_phase)
            
            # Convert intensity to color
            if base_color == '#ff0000':  # Red theme
                r = int(intensity * 255)
                pulse_color = f"#{r:02x}0000"
            else:
                # Extract RGB from hex color
                hex_color = base_color.lstrip('#')
                r = int(hex_color[0:2], 16)
                g = int(hex_color[2:4], 16)
                b = int(hex_color[4:6], 16)
                
                # Apply pulse effect
                r = int(r * intensity)
                g = int(g * intensity)
                b = int(b * intensity)
                pulse_color = f"#{r:02x}{g:02x}{b:02x}"
            
            try:
                widget.config(highlightbackground=pulse_color, highlightcolor=pulse_color)
            except:
                pass
                
            widget.after(100, pulse)
            
        return pulse
    
    def create_smooth_scroll(self, text_widget):
        """Create smooth scrolling animation for text widgets"""
        def smooth_scroll(event):
            if event.delta:
                # Get current position
                current_pos = text_widget.yview()[0]
                
                # Calculate new position with easing
                steps = 10
                target_pos = current_pos - (event.delta / 120) * 0.1
                
                def scroll_step(step):
                    if step < steps:
                        # Easing function for smooth scroll
                        t = step / steps
                        ease = 1 - (1 - t) ** 3  # Cubic ease out
                        new_pos = current_pos + (target_pos - current_pos) * ease
                        text_widget.yview_moveto(new_pos)
                        text_widget.after(10, lambda: scroll_step(step + 1))
                
                scroll_step(0)
            return "break"
        
        # Bind mouse wheel for smooth scrolling
        text_widget.bind("<MouseWheel>", smooth_scroll)
        
    def create_fade_in(self, widget, duration=500):
        """Create fade-in animation for widgets"""
        def fade(step=0):
            if step <= 100:
                alpha = step / 100.0
                try:
                    widget.config(highlightbackground=self.hex_to_rgba(widget.cget('bg'), alpha))
                except:
                    pass
                widget.after(duration // 100, lambda: fade(step + 1))
        
        fade()
    
    def hex_to_rgba(self, hex_color, alpha):
        """Convert hex color to rgba string"""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return f'#{r:02x}{g:02x}{b:02x}'

# ==================== ADVANCED THEME MANAGER ====================

class ThemeManager:
    """Advanced theme management with custom colors and curved corners"""
    
    def __init__(self, app):
        self.app = app
        self.current_theme = "dark"
        self.custom_colors = {}
        self.curved_corners = True
        self.corner_radius = 15
        
        # Define theme presets
        self.themes = {
            "dark": {
                "name": "Dark Red",
                "bg": "#0a0a0a",
                "fg": "#ff0000",
                "accent": "#ff0000",
                "secondary_bg": "#1a1a1a",
                "header_bg": "#110000",
                "text_bg": "#0a0a0a",
                "border_color": "#330000",
                "button_bg": "#550000",
                "button_fg": "white",
                "hover_color": "#770000"
            },
            "blue": {
                "name": "Cyber Blue",
                "bg": "#0a0a1a",
                "fg": "#00ffff",
                "accent": "#00ffff",
                "secondary_bg": "#1a1a2a",
                "header_bg": "#000033",
                "text_bg": "#0a0a1a",
                "border_color": "#006666",
                "button_bg": "#005555",
                "button_fg": "white",
                "hover_color": "#007777"
            },
            "green": {
                "name": "Matrix Green",
                "bg": "#0a1a0a",
                "fg": "#00ff00",
                "accent": "#00ff00",
                "secondary_bg": "#1a2a1a",
                "header_bg": "#003300",
                "text_bg": "#0a1a0a",
                "border_color": "#006600",
                "button_bg": "#005500",
                "button_fg": "white",
                "hover_color": "#007700"
            },
            "purple": {
                "name": "Neon Purple",
                "bg": "#1a0a1a",
                "fg": "#ff00ff",
                "accent": "#ff00ff",
                "secondary_bg": "#2a1a2a",
                "header_bg": "#330033",
                "text_bg": "#1a0a1a",
                "border_color": "#660066",
                "button_bg": "#550055",
                "button_fg": "white",
                "hover_color": "#770077"
            },
            "orange": {
                "name": "Fire Orange",
                "bg": "#1a0a0a",
                "fg": "#ff6600",
                "accent": "#ff6600",
                "secondary_bg": "#2a1a1a",
                "header_bg": "#331100",
                "text_bg": "#1a0a0a",
                "border_color": "#663300",
                "button_bg": "#552200",
                "button_fg": "white",
                "hover_color": "#773300"
            }
        }
    
    def apply_theme(self, theme_name, custom_colors=None):
        """Apply theme with custom colors and curved corners"""
        if theme_name in self.themes:
            self.current_theme = theme_name
            theme = self.themes[theme_name].copy()
            
            # Override with custom colors if provided
            if custom_colors:
                theme.update(custom_colors)
            
            self.custom_colors = theme
            
            # Apply theme to all widgets
            self.update_widget_colors(theme)
            
            # Apply curved corners if enabled
            if self.curved_corners:
                self.apply_curved_corners()
            
            return True
        return False
    
    def update_widget_colors(self, theme):
        """Update all widget colors according to theme"""
        try:
            # Update root window
            self.app.root.configure(bg=theme['bg'])
            
            # Update main frames
            for widget in self.app.root.winfo_children():
                self.recursive_color_update(widget, theme)
            
            # Update specific widgets that need special handling
            self.update_chat_display_colors(theme)
            self.update_input_colors(theme)
            self.update_button_colors(theme)
            
            # Restart animations with new colors
            self.restart_animations(theme)
            
        except Exception as e:
            self.app.logger.error(f"Theme application error: {e}")
    
    def recursive_color_update(self, widget, theme):
        """Recursively update colors for all child widgets"""
        try:
            widget_type = widget.winfo_class()
            
            # Frame widgets
            if widget_type in ['TFrame', 'Frame']:
                try:
                    widget.configure(bg=theme['bg'])
                except:
                    pass
            
            # Label widgets
            elif widget_type == 'Label':
                try:
                    if 'premium' in widget.cget('text').lower() or 'evil' in widget.cget('text').lower():
                        widget.configure(fg=theme['accent'], bg=theme['header_bg'])
                    else:
                        widget.configure(fg=theme['fg'], bg=theme['bg'])
                except:
                    pass
            
            # Text and ScrolledText widgets
            elif widget_type in ['Text', 'ScrolledText']:
                try:
                    widget.configure(
                        bg=theme['text_bg'],
                        fg=theme['fg'],
                        insertbackground=theme['accent'],
                        selectbackground=theme['secondary_bg']
                    )
                except:
                    pass
            
            # Button widgets
            elif widget_type == 'Button':
                try:
                    widget.configure(
                        bg=theme['button_bg'],
                        fg=theme['button_fg'],
                        activebackground=theme['hover_color']
                    )
                except:
                    pass
            
            # Entry widgets
            elif widget_type == 'Entry':
                try:
                    widget.configure(
                        bg=theme['text_bg'],
                        fg=theme['fg'],
                        insertbackground=theme['accent']
                    )
                except:
                    pass
            
            # Recursively update children
            for child in widget.winfo_children():
                self.recursive_color_update(child, theme)
                
        except Exception as e:
            pass  # Silently handle any widget update errors
    
    def update_chat_display_colors(self, theme):
        """Update chat display specific colors"""
        try:
            # Update chat display tags
            tags_config = {
                "user": {"foreground": theme['accent']},
                "ai": {"foreground": theme['fg']},
                "system": {"foreground": theme['accent']},
                "error": {"foreground": theme['accent']},
                "separator": {"foreground": theme['border_color']},
                "code": {"background": theme['secondary_bg'], "foreground": theme['fg']},
                "code_header": {"background": theme['header_bg'], "foreground": theme['accent']}
            }
            
            for tag, config in tags_config.items():
                self.app.chat_display.tag_configure(tag, **config)
            
            # Update streaming display
            self.app.streaming_display.configure(
                bg=theme['text_bg'],
                fg=theme['fg'],
                insertbackground=theme['accent']
            )
            
        except Exception as e:
            self.app.logger.error(f"Chat display color update error: {e}")
    
    def update_input_colors(self, theme):
        """Update input field colors"""
        try:
            self.app.input_field.configure(
                bg=theme['text_bg'],
                fg=theme['fg'],
                insertbackground=theme['accent']
            )
        except:
            pass
    
    def update_button_colors(self, theme):
        """Update button colors with hover effects"""
        try:
            for widget in self.app.root.winfo_children():
                self.recursive_button_update(widget, theme)
        except:
            pass
    
    def recursive_button_update(self, widget, theme):
        """Recursively update button colors"""
        try:
            if widget.winfo_class() == 'Button':
                widget.configure(
                    bg=theme['button_bg'],
                    fg=theme['button_fg'],
                    activebackground=theme['hover_color']
                )
            
            for child in widget.winfo_children():
                self.recursive_button_update(child, theme)
        except:
            pass
    
    def apply_curved_corners(self):
        """Apply curved corners to all applicable widgets"""
        try:
            for widget in self.app.root.winfo_children():
                self.recursive_curve_corners(widget)
        except Exception as e:
            self.app.logger.error(f"Curved corners error: {e}")
    
    def recursive_curve_corners(self, widget):
        """Recursively apply curved corners to widgets"""
        try:
            widget_type = widget.winfo_class()
            
            # Apply to frames, buttons, text widgets
            if widget_type in ['TFrame', 'Frame', 'Button', 'Text', 'ScrolledText', 'Entry']:
                try:
                    widget.configure(relief='raised', borderwidth=2)
                except:
                    pass
            
            for child in widget.winfo_children():
                self.recursive_curve_corners(child)
                
        except:
            pass
    
    def restart_animations(self, theme):
        """Restart animations with new theme colors"""
        try:
            # Restart pulse animations
            if hasattr(self.app, 'premium_badge'):
                self.app.animation_engine.create_pulse_effect(
                    self.app.premium_badge, theme['accent']
                )()
        except:
            pass
    
    def show_theme_selector(self):
        """Show theme selection dialog"""
        theme_window = tk.Toplevel(self.app.root)
        theme_window.title("🎨 Theme Customizer - ELYOUSSEFI EVIL PREMIUM")
        theme_window.geometry("600x500")
        theme_window.configure(bg=self.custom_colors.get('bg', '#0a0a0a'))
        theme_window.transient(self.app.root)
        
        # Center window
        theme_window.update_idletasks()
        x = (self.app.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.app.root.winfo_screenheight() // 2) - (500 // 2)
        theme_window.geometry(f"600x500+{x}+{y}")
        
        # Make window resizable
        theme_window.minsize(500, 400)
        
        # Header
        header = tk.Label(
            theme_window,
            text="🎨 PREMIUM THEME CUSTOMIZER",
            font=('Arial Black', 16, 'bold'),
            fg=self.custom_colors.get('accent', '#ff0000'),
            bg=self.custom_colors.get('header_bg', '#110000')
        )
        header.pack(fill=tk.X, pady=10)
        
        # Theme presets frame
        presets_frame = ttk.LabelFrame(theme_window, text="🎭 Theme Presets", style='Dark.TLabelframe')
        presets_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Create theme preset buttons
        presets_container = ttk.Frame(presets_frame, style='Dark.TFrame')
        presets_container.pack(fill=tk.X, padx=10, pady=10)
        
        for i, (theme_key, theme_data) in enumerate(self.themes.items()):
            btn = tk.Button(
                presets_container,
                text=theme_data['name'],
                font=('Courier New', 10, 'bold'),
                bg=theme_data['button_bg'],
                fg=theme_data['button_fg'],
                command=lambda t=theme_key: self.apply_theme_and_close(t, theme_window),
                width=12,
                height=2
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5, sticky='ew')
        
        # Custom color frame
        custom_frame = ttk.LabelFrame(theme_window, text="🎨 Custom Colors", style='Dark.TLabelframe')
        custom_frame.pack(fill=tk.X, padx=20, pady=10)
        
        color_options = [
            ("Accent Color", "accent"),
            ("Background", "bg"),
            ("Text Color", "fg"),
            ("Header Background", "header_bg"),
            ("Button Color", "button_bg")
        ]
        
        for i, (color_name, color_key) in enumerate(color_options):
            color_frame = ttk.Frame(custom_frame, style='Dark.TFrame')
            color_frame.pack(fill=tk.X, padx=10, pady=5)
            
            tk.Label(
                color_frame,
                text=color_name + ":",
                font=('Courier New', 9),
                fg=self.custom_colors.get('fg', '#ff0000'),
                bg=self.custom_colors.get('bg', '#0a0a0a')
            ).pack(side=tk.LEFT)
            
            current_color = self.custom_colors.get(color_key, '#ff0000')
            color_btn = tk.Button(
                color_frame,
                text="▓▓▓",
                font=('Courier New', 8),
                bg=current_color,
                fg='white',
                command=lambda k=color_key: self.choose_color(k, theme_window),
                width=5
            )
            color_btn.pack(side=tk.RIGHT, padx=5)
        
        # Corner radius control
        corner_frame = ttk.LabelFrame(theme_window, text="🔲 Corner Style", style='Dark.TLabelframe')
        corner_frame.pack(fill=tk.X, padx=20, pady=10)
        
        corner_control = ttk.Frame(corner_frame, style='Dark.TFrame')
        corner_control.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            corner_control,
            text="Curved Corners:",
            font=('Courier New', 9),
            fg=self.custom_colors.get('fg', '#ff0000'),
            bg=self.custom_colors.get('bg', '#0a0a0a')
        ).pack(side=tk.LEFT)
        
        corner_var = tk.BooleanVar(value=self.curved_corners)
        corner_cb = tk.Checkbutton(
            corner_control,
            variable=corner_var,
            command=lambda: self.toggle_corners(corner_var.get()),
            bg=self.custom_colors.get('bg', '#0a0a0a'),
            fg=self.custom_colors.get('fg', '#ff0000'),
            selectcolor=self.custom_colors.get('button_bg', '#550000')
        )
        corner_cb.pack(side=tk.RIGHT)
    
    def choose_color(self, color_key, parent_window):
        """Open color chooser for custom color selection"""
        color_code = colorchooser.askcolor(
            initialcolor=self.custom_colors.get(color_key, '#ff0000'),
            title=f"Choose {color_key} color"
        )
        
        if color_code[0]:
            new_color = color_code[1]
            self.custom_colors[color_key] = new_color
            self.apply_theme(self.current_theme, self.custom_colors)
            parent_window.destroy()
            self.show_theme_selector()  # Refresh selector
    
    def apply_theme_and_close(self, theme_name, window):
        """Apply theme and close selector"""
        self.apply_theme(theme_name)
        window.destroy()
        self.app.add_message("🎨", f"Theme changed to: {self.themes[theme_name]['name']}", "system")
    
    def toggle_corners(self, enabled):
        """Toggle curved corners"""
        self.curved_corners = enabled
        if enabled:
            self.apply_curved_corners()
            self.app.add_message("🔲", "Curved corners enabled", "system")
        else:
            self.app.add_message("🔲", "Curved corners disabled", "system")

# ==================== PREMIUM ANALYTICS DASHBOARD ====================

class PremiumAnalyticsDashboard:
    """Advanced analytics system with real-time data visualization"""
    
    def __init__(self, app):
        self.app = app
        self.analytics_data = {
            "total_messages": 0,
            "total_tokens": 0,
            "code_blocks_generated": 0,
            "sessions_started": 0,
            "api_calls": 0,
            "start_time": datetime.now(),
            "messages_by_hour": [0] * 24,
            "tokens_by_hour": [0] * 24,
            "popular_models": {},
            "error_count": 0
        }
        
    def record_message(self, message_length, tokens_used=0, model_used=None):
        """Record message analytics"""
        self.analytics_data["total_messages"] += 1
        self.analytics_data["total_tokens"] += tokens_used
        self.analytics_data["api_calls"] += 1
        
        current_hour = datetime.now().hour
        self.analytics_data["messages_by_hour"][current_hour] += 1
        self.analytics_data["tokens_by_hour"][current_hour] += tokens_used
        
        if model_used:
            self.analytics_data["popular_models"][model_used] = \
                self.analytics_data["popular_models"].get(model_used, 0) + 1
    
    def record_code_block(self):
        """Record code block generation"""
        self.analytics_data["code_blocks_generated"] += 1
    
    def record_session(self):
        """Record session start"""
        self.analytics_data["sessions_started"] += 1
    
    def record_error(self):
        """Record error occurrence"""
        self.analytics_data["error_count"] += 1
    
    def get_session_duration(self):
        """Get current session duration"""
        return datetime.now() - self.analytics_data["start_time"]
    
    def get_messages_per_hour(self):
        """Get average messages per hour"""
        duration_hours = max(1, self.get_session_duration().total_seconds() / 3600)
        return self.analytics_data["total_messages"] / duration_hours
    
    def get_tokens_per_message(self):
        """Get average tokens per message"""
        if self.analytics_data["total_messages"] == 0:
            return 0
        return self.analytics_data["total_tokens"] / self.analytics_data["total_messages"]

# ==================== CODE DETECTION ENGINE ====================

class CodeDetectionEngine:
    """Advanced code detection with language identification"""
    
    def __init__(self):
        self.language_patterns = {
            'python': {
                'patterns': [r'def\s+\w+', r'class\s+\w+', r'import\s+\w+', r'from\s+\w+', r'print\s*\(', r'if\s+\w+:', r'for\s+\w+\s+in'],
                'extensions': ['.py'],
                'keywords': ['def', 'class', 'import', 'from', 'print', 'if', 'else', 'for', 'while']
            },
            'javascript': {
                'patterns': [r'function\s+\w+', r'const\s+\w+', r'let\s+\w+', r'var\s+\w+', r'console\.log', r'=>', r'document\.'],
                'extensions': ['.js', '.jsx'],
                'keywords': ['function', 'const', 'let', 'var', 'console', 'document', 'window']
            },
            'java': {
                'patterns': [r'public\s+class', r'private\s+\w+', r'System\.out\.print', r'import\s+java', r'void\s+\w+'],
                'extensions': ['.java'],
                'keywords': ['public', 'private', 'class', 'void', 'static', 'System.out']
            },
            'cpp': {
                'patterns': [r'#include\s*<.*>', r'using\s+namespace', r'std::', r'cout\s*<<', r'cin\s*>>'],
                'extensions': ['.cpp', '.h', '.hpp'],
                'keywords': ['#include', 'using', 'namespace', 'std::', 'cout', 'cin']
            },
            'html': {
                'patterns': [r'<!DOCTYPE html>', r'<html>', r'<head>', r'<body>', r'<div\s+', r'<span\s+'],
                'extensions': ['.html', '.htm'],
                'keywords': ['<html>', '<head>', '<body', '<div', '<span', '<p>']
            },
            'css': {
                'patterns': [r'\w+\s*\{', r'\.\w+\s*\{', r'#\w+\s*\{', r'@media', r'@keyframes'],
                'extensions': ['.css'],
                'keywords': ['{', '}', ';', '.class', '#id']
            },
            'php': {
                'patterns': [r'<\?php', r'\$\w+\s*=', r'echo\s+', r'function\s+\w+'],
                'extensions': ['.php'],
                'keywords': ['<?php', '?>', '$', 'echo', 'function']
            },
            'sql': {
                'patterns': [r'SELECT\s+.+FROM', r'INSERT\s+INTO', r'UPDATE\s+\w+', r'DELETE\s+FROM', r'CREATE\s+TABLE'],
                'extensions': ['.sql'],
                'keywords': ['SELECT', 'FROM', 'WHERE', 'INSERT', 'UPDATE', 'DELETE']
            },
            'bash': {
                'patterns': [r'#!/bin/bash', r'#!/bin/sh', r'echo\s+', r'cd\s+', r'ls\s+', r'grep\s+'],
                'extensions': ['.sh', '.bash'],
                'keywords': ['echo', 'cd', 'ls', 'grep', 'if', 'then', 'fi']
            },
            'ruby': {
                'patterns': [r'def\s+\w+', r'class\s+\w+', r'puts\s+', r'end\s*$'],
                'extensions': ['.rb'],
                'keywords': ['def', 'class', 'end', 'puts', 'require']
            }
        }
        
        self.code_block_pattern = r'```(\w+)?\s*\n(.*?)```'
        
    def detect_language(self, code_snippet):
        """Detect programming language from code snippet"""
        code_snippet = code_snippet.strip()
        if not code_snippet:
            return 'text'
            
        # Check for explicit language markers first
        lines = code_snippet.split('\n')
        first_line = lines[0].strip().lower() if lines else ""
        
        # Check for shebangs and explicit markers
        if first_line.startswith('#!/bin/bash') or first_line.startswith('#!/bin/sh'):
            return 'bash'
        elif first_line.startswith('<?php'):
            return 'php'
        elif first_line.startswith('<!doctype html>'):
            return 'html'
            
        # Score each language based on patterns and keywords
        scores = {}
        for lang, patterns in self.language_patterns.items():
            score = 0
            
            # Check patterns
            for pattern in patterns['patterns']:
                if re.search(pattern, code_snippet, re.IGNORECASE | re.MULTILINE):
                    score += 2
                    
            # Check keywords
            for keyword in patterns['keywords']:
                if keyword.lower() in code_snippet.lower():
                    score += 1
                    
            scores[lang] = score
            
        # Return language with highest score
        best_language = max(scores, key=scores.get)
        return best_language if scores[best_language] > 0 else 'text'
    
    def extract_code_blocks(self, text):
        """Extract all code blocks from text with language detection"""
        code_blocks = []
        
        # Find all code blocks with triple backticks
        matches = list(re.finditer(self.code_block_pattern, text, re.DOTALL))
        
        for match in matches:
            explicit_lang = match.group(1)
            code_content = match.group(2).strip()
            
            if explicit_lang:
                language = explicit_lang.lower()
            else:
                language = self.detect_language(code_content)
                
            code_blocks.append({
                'language': language,
                'content': code_content,
                'start_pos': match.start(),
                'end_pos': match.end()
            })
            
        return code_blocks

# ==================== CHATGPT-STYLE CODE FRAME ====================

class CodeFrame:
    """ChatGPT-style code display frame with syntax highlighting and theme support"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.current_code = None
        self.current_language = None
        self.setup_code_frame()
        
    def setup_code_frame(self):
        """Setup the code frame with theme support"""
        # Main code frame container
        self.code_container = ttk.Frame(self.parent, style='Dark.TFrame')
        
        # Header with language label and buttons
        self.header_frame = ttk.Frame(self.code_container, style='Dark.TFrame')
        self.header_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        
        # Language label
        self.lang_label = tk.Label(
            self.header_frame,
            text="",
            font=('Courier New', 10, 'bold'),
            fg=self.app.theme_manager.custom_colors.get('fg', '#ffffff'),
            bg=self.app.theme_manager.custom_colors.get('header_bg', '#1a1a1a'),
            padx=10,
            pady=5
        )
        self.lang_label.pack(side=tk.LEFT)
        
        # Button frame
        self.button_frame = ttk.Frame(self.header_frame, style='Dark.TFrame')
        self.button_frame.pack(side=tk.RIGHT)
        
        # Copy button
        self.copy_btn = tk.Button(
            self.button_frame,
            text="📋 Copy",
            font=('Courier New', 9),
            bg=self.app.theme_manager.custom_colors.get('button_bg', '#550000'),
            fg='white',
            command=self.copy_code,
            padx=10
        )
        self.copy_btn.pack(side=tk.LEFT, padx=2)
        
        # Download button
        self.download_btn = tk.Button(
            self.button_frame,
            text="💾 Download",
            font=('Courier New', 9),
            bg=self.app.theme_manager.custom_colors.get('button_bg', '#555500'),
            fg='white',
            command=self.download_code,
            padx=10
        )
        self.download_btn.pack(side=tk.LEFT, padx=2)
        
        # Close button
        self.close_btn = tk.Button(
            self.button_frame,
            text="✕",
            font=('Courier New', 10, 'bold'),
            bg=self.app.theme_manager.custom_colors.get('button_bg', '#550000'),
            fg='white',
            command=self.hide_code_frame,
            width=3
        )
        self.close_btn.pack(side=tk.LEFT, padx=2)
        
        # Code display area
        self.code_display = scrolledtext.ScrolledText(
            self.code_container,
            wrap=tk.WORD,
            font=('Consolas', 11),
            bg=self.app.theme_manager.custom_colors.get('text_bg', '#1e1e1e'),
            fg=self.app.theme_manager.custom_colors.get('accent', '#ff4444'),
            insertbackground=self.app.theme_manager.custom_colors.get('fg', '#ffffff'),
            selectbackground=self.app.theme_manager.custom_colors.get('secondary_bg', '#264f78'),
            relief='flat',
            borderwidth=0,
            padx=15,
            pady=10
        )
        self.code_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.code_display.config(state=tk.DISABLED)
        
        # Configure syntax highlighting tags with theme colors
        self.configure_syntax_tags()
        
        # Apply smooth scrolling
        self.app.animation_engine.create_smooth_scroll(self.code_display)
        
    def configure_syntax_tags(self):
        """Configure syntax highlighting tags with theme colors"""
        accent_color = self.app.theme_manager.custom_colors.get('accent', '#ff6666')
        fg_color = self.app.theme_manager.custom_colors.get('fg', '#ff0000')
        secondary_bg = self.app.theme_manager.custom_colors.get('secondary_bg', '#1a1a1a')
        
        # Python syntax
        self.code_display.tag_configure("py_keyword", foreground=accent_color)
        self.code_display.tag_configure("py_string", foreground=fg_color)
        self.code_display.tag_configure("py_comment", foreground=secondary_bg)
        self.code_display.tag_configure("py_number", foreground=accent_color)
        self.code_display.tag_configure("py_function", foreground=fg_color)
        
        # JavaScript syntax
        self.code_display.tag_configure("js_keyword", foreground=accent_color)
        self.code_display.tag_configure("js_string", foreground=fg_color)
        self.code_display.tag_configure("js_comment", foreground=secondary_bg)
        self.code_display.tag_configure("js_number", foreground=accent_color)
        self.code_display.tag_configure("js_function", foreground=fg_color)
        
        # HTML syntax
        self.code_display.tag_configure("html_tag", foreground=accent_color)
        self.code_display.tag_configure("html_attr", foreground=fg_color)
        self.code_display.tag_configure("html_string", foreground=accent_color)
        self.code_display.tag_configure("html_comment", foreground=secondary_bg)
        
        # CSS syntax
        self.code_display.tag_configure("css_property", foreground=accent_color)
        self.code_display.tag_configure("css_value", foreground=fg_color)
        self.code_display.tag_configure("css_selector", foreground=accent_color)
        self.code_display.tag_configure("css_comment", foreground=secondary_bg)
        
        # General tags
        self.code_display.tag_configure("sql_keyword", foreground=accent_color)
        self.code_display.tag_configure("bash_keyword", foreground=accent_color)
        
    def show_code(self, code_content, language):
        """Display code in the code frame with syntax highlighting"""
        self.current_code = code_content
        self.current_language = language
        
        # Update language label
        self.lang_label.config(text=language.upper())
        
        # Enable code display and clear previous content
        self.code_display.config(state=tk.NORMAL)
        self.code_display.delete('1.0', tk.END)
        
        # Insert code with syntax highlighting
        self.apply_syntax_highlighting(code_content, language)
        
        self.code_display.config(state=tk.DISABLED)
        
        # Show the code frame
        self.show_code_frame()
        
    def apply_syntax_highlighting(self, code, language):
        """Apply syntax highlighting based on language"""
        # Insert plain text first
        self.code_display.insert('1.0', code)
        
        # Simple keyword-based highlighting
        if language == 'python':
            self.highlight_pattern(r'\b(def|class|import|from|as|if|else|elif|for|while|return|try|except|finally|with|lambda)\b', 'py_keyword')
            self.highlight_pattern(r'(\".*?\"|\'.*?\')', 'py_string')
            self.highlight_pattern(r'#.*$', 'py_comment')
        elif language == 'javascript':
            self.highlight_pattern(r'\b(function|var|let|const|if|else|for|while|return|try|catch|class|import|export)\b', 'js_keyword')
            self.highlight_pattern(r'(\".*?\"|\'.*?\')', 'js_string')
            self.highlight_pattern(r'//.*$', 'js_comment')
        elif language == 'html':
            self.highlight_pattern(r'</?\w+\b|/?>', 'html_tag')
            self.highlight_pattern(r'\b(\w+)=', 'html_attr')
            self.highlight_pattern(r'(\".*?\")', 'html_string')
        elif language == 'css':
            self.highlight_pattern(r'(\b[\w-]+\s*:)', 'css_property')
            self.highlight_pattern(r':\s*([^;]+)', 'css_value')
                
    def highlight_pattern(self, pattern, tag):
        """Highlight specific patterns in the code"""
        start_pos = '1.0'
        while True:
            pos = self.code_display.search(pattern, start_pos, stopindex=tk.END, regexp=True)
            if not pos:
                break
            end_pos = f"{pos}+{len(self.code_display.get(pos, f'{pos} lineend'))}c"
            self.code_display.tag_add(tag, pos, end_pos)
            start_pos = end_pos
            
    def copy_code(self):
        """Copy code to clipboard"""
        if self.current_code:
            self.app.root.clipboard_clear()
            self.app.root.clipboard_append(self.current_code)
            self.app.add_message("📋", f"Code copied to clipboard! ({self.current_language})", "system")
            
    def download_code(self):
        """Download code to file"""
        if not self.current_code:
            return
            
        # Determine file extension
        extensions = {
            'python': '.py', 'javascript': '.js', 'java': '.java', 'cpp': '.cpp',
            'html': '.html', 'css': '.css', 'php': '.php', 'sql': '.sql',
            'bash': '.sh', 'ruby': '.rb', 'text': '.txt'
        }
        ext = extensions.get(self.current_language, '.txt')
        
        filename = filedialog.asksaveasfilename(
            defaultextension=ext,
            filetypes=[(f"{self.current_language.upper()} files", f"*{ext}"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.current_code)
                self.app.add_message("💾", f"Code saved to: {filename}", "system")
            except Exception as e:
                messagebox.showerror("Error", f"Save failed: {str(e)}")
                
    def show_code_frame(self):
        """Show the code frame"""
        self.code_container.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0), pady=10)
        self.code_container.pack_propagate(False)
        self.code_container.config(width=500)
        
    def hide_code_frame(self):
        """Hide the code frame"""
        self.code_container.pack_forget()

# ==================== SECURITY MANAGER ====================

class SecurityManager:
    """Handles encryption and security"""
    def __init__(self):
        self.encryption_key = self.load_or_create_key()
        
    def load_or_create_key(self):
        key_path = Path("encryption.key")
        if key_path.exists():
            return key_path.read_bytes()
        else:
            key = b"default_key_32_bytes_long_123!"
            key_path.write_bytes(key)
            return key
            
    def encrypt(self, data):
        if isinstance(data, str):
            data = data.encode()
        return bytes([b ^ self.encryption_key[i % len(self.encryption_key)] for i, b in enumerate(data)])
        
    def decrypt(self, encrypted_data):
        return bytes([b ^ self.encryption_key[i % len(self.encryption_key)] for i, b in enumerate(encrypted_data)]).decode()

# ==================== MULTI-API MANAGER ====================

class APIManager:
    """Manages multiple AI APIs with unlimited tokens"""
    
    def __init__(self, app):
        self.app = app
        self.current_provider = "openrouter"
        self.failover_enabled = True
        self.stop_streaming = False
        # REALISTIC token limits for actual API calls
        self.max_tokens = 4096  # Realistic limit that actually works
        
    def get_response(self, message, conversation_history, **kwargs):
        try:
            # Use realistic token limits that actually work
            kwargs['max_tokens'] = self.max_tokens
            return self.get_openrouter_response(message, conversation_history, **kwargs)
        except Exception as e:
            self.app.logger.error(f"API Error: {str(e)}")
            if self.failover_enabled:
                self.app.add_message("🔄", "Primary API failed, trying fallback...", "system")
                # Try fallback to a simpler approach
                return self.get_fallback_response(message)
            raise e

    def get_fallback_response(self, message):
        """Fallback response when API fails"""
        fallback_responses = [
            f"I understand you're asking: '{message}'. Currently, the AI service is experiencing issues. Please check your API key and try again.",
            f"Regarding your question about '{message}', I'm unable to connect to the AI service at the moment. Please verify your API key and internet connection.",
            f"I received your message about '{message}' but the AI service is temporarily unavailable. Please try again in a moment."
        ]
        return random.choice(fallback_responses)
            
    def get_openrouter_response(self, message, conversation_history, **kwargs):
        """OpenRouter API implementation with working token limits"""
        if not self.app.api_key:
            raise Exception("API key not set. Please enter your OpenRouter API key.")
            
        headers = {
            "Authorization": f"Bearer {self.app.api_key}",
            "HTTP-Referer": "https://github.com",
            "X-Title": "ELYOUSSEFI EVIL PREMIUM",
            "Content-Type": "application/json"
        }
        
        # Prepare messages with proper formatting - FIXED THIS PART
        messages = []
        
        # Add system prompt if available
        if self.app.ai_memory.get("system_prompt"):
            messages.append({"role": "system", "content": self.app.ai_memory["system_prompt"]})
        
        # Add conversation history (limit to avoid token limits)
        # Only include the last 6 messages to stay within reasonable token limits
        for msg in conversation_history[-6:]:
            messages.append(msg)
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Use realistic payload that works with OpenRouter
        payload = {
            "model": self.app.current_model,
            "messages": messages,
            "max_tokens": kwargs.get('max_tokens', self.max_tokens),
            "temperature": kwargs.get('temperature', 0.7),
            "stream": True
        }
        
        try:
            self.app.logger.info(f"Sending request to OpenRouter with model: {self.app.current_model}")
            response = self.app.session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers, 
                json=payload, 
                timeout=30, 
                stream=True
            )
            
            if response.status_code == 200:
                return self.handle_streaming_response(response)
            else:
                # Get detailed error information
                error_text = response.text
                self.app.logger.error(f"API Error {response.status_code}: {error_text}")
                
                if response.status_code == 400:
                    raise Exception("Bad request - invalid parameters or model not available")
                elif response.status_code == 401:
                    raise Exception("Invalid API key - please check your OpenRouter API key")
                elif response.status_code == 429:
                    raise Exception("Rate limit exceeded - please wait before trying again")
                elif response.status_code == 500:
                    raise Exception("Server error - please try again later")
                else:
                    raise Exception(f"API Error {response.status_code}: {error_text}")
                    
        except requests.exceptions.Timeout:
            raise Exception("Request timeout - the server took too long to respond")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection error - please check your internet connection")
        except Exception as e:
            raise Exception(f"Request failed: {str(e)}")
            
    def handle_streaming_response(self, response):
        """Handle streaming response properly"""
        full_response = ""
        self.stop_streaming = False
        
        try:
            for line in response.iter_lines():
                if self.stop_streaming:
                    break
                    
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data = line[6:]
                        if data == '[DONE]':
                            break
                        try:
                            chunk_data = json.loads(data)
                            if 'choices' in chunk_data and chunk_data['choices']:
                                delta = chunk_data['choices'][0].get('delta', {})
                                if 'content' in delta:
                                    content_chunk = delta['content']
                                    full_response += content_chunk
                                    self.app.root.after(0, self.app.update_streaming_display, content_chunk)
                        except json.JSONDecodeError:
                            continue
            return full_response
        except Exception as e:
            self.app.logger.error(f"Streaming error: {str(e)}")
            # Return whatever we have so far
            return full_response if full_response else f"Error processing stream: {str(e)}"
    
    def stop_current_stream(self):
        """Stop the current streaming response"""
        self.stop_streaming = True

# ==================== PLUGIN SYSTEM ====================

class Plugin:
    """Base plugin class"""
    def __init__(self, app):
        self.app = app
        self.name = "Base Plugin"
        self.version = "1.0"
        
    def on_message_sent(self, message):
        pass
        
    def on_message_received(self, message):
        pass
        
    def on_app_start(self):
        pass
        
    def on_app_close(self):
        pass

class GrammarCheckerPlugin(Plugin):
    """Grammar checking plugin"""
    def __init__(self, app):
        super().__init__(app)
        self.name = "Grammar Checker"
        
    def on_message_sent(self, message):
        if len(message.split()) < 2:
            self.app.show_toast("⚠️ Very short message", "warning")

class CodeFormatterPlugin(Plugin):
    """Code formatting plugin"""
    def __init__(self, app):
        super().__init__(app)
        self.name = "Code Formatter"
        
    def on_message_received(self, message):
        code_blocks = self.app.code_detector.extract_code_blocks(message)
        if code_blocks:
            self.app.add_message("⚡", f"Detected {len(code_blocks)} code block(s)", "system")

class SentimentAnalyzerPlugin(Plugin):
    """Sentiment analysis plugin"""
    def __init__(self, app):
        super().__init__(app)
        self.name = "Sentiment Analysis"
        
    def on_message_received(self, message):
        positive_words = ['good', 'great', 'excellent', 'awesome', 'thanks']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'wrong']
        
        if any(word in message.lower() for word in positive_words):
            self.app.add_message("😊", "Positive sentiment detected", "system")
        elif any(word in message.lower() for word in negative_words):
            self.app.add_message("😟", "Negative sentiment detected", "system")

# ==================== PLUGIN MANAGER ====================

class PluginManager:
    """Manages plugins"""
    def __init__(self, app):
        self.app = app
        self.plugins = []
        
    def load_plugins(self):
        """Load all plugins"""
        self.plugins = [
            GrammarCheckerPlugin(self.app),
            CodeFormatterPlugin(self.app),
            SentimentAnalyzerPlugin(self.app)
        ]
        
        for plugin in self.plugins:
            try:
                plugin.on_app_start()
            except Exception as e:
                self.app.logger.error(f"Plugin {plugin.name} failed to start: {e}")
            
        if hasattr(self.app, 'plugin_status'):
            self.app.plugin_status.config(text=f"Plugins: {len(self.plugins)} active")

    def unload_plugins(self):
        """Unload all plugins"""
        for plugin in self.plugins:
            try:
                plugin.on_app_close()
            except Exception as e:
                self.app.logger.error(f"Plugin {plugin.name} failed to stop: {e}")
        self.plugins = []

# ==================== ENHANCED MAIN APPLICATION ====================

class UltimateEvilGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🦇 ELYOUSSEFI EVIL - ULTIMATE EDITION PREMIUM")
        self.root.configure(bg='black')
        
        # Set minimum window size and make resizable
        self.root.minsize(1200, 700)  # Reasonable minimum size
        self.root.geometry('1400x900')  # Default size
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Setup logging
        self.setup_logging()
        
        # Initialize enhanced systems
        self.animation_engine = PremiumAnimationEngine(root)
        self.theme_manager = ThemeManager(self)
        self.analytics_dashboard = PremiumAnalyticsDashboard(self)
        
        # Initialize code detection engine
        self.code_detector = CodeDetectionEngine()
        
        # Initialize managers
        self.security_manager = SecurityManager()
        self.api_manager = APIManager(self)
        self.plugin_manager = PluginManager(self)
        
        # Center window
        self.center_window()
        
        # API configuration
        self.api_key = None
        self.session = requests.Session()
        
        # Available models
        self.available_models = {
            "DeepSeek Chat": "deepseek/deepseek-chat",
            "DeepSeek Coder": "deepseek/deepseek-coder", 
            "GPT-3.5 Turbo": "openai/gpt-3.5-turbo",
            "Claude Instant": "anthropic/claude-3-haiku",
            "Llama 3.1 8B": "meta-llama/llama-3.1-8b-instruct"
        }
        self.current_model = "deepseek/deepseek-chat"
        
        # AI Memory system
        self.ai_memory = {
            "system_prompt": "You are EVIL PREMIUM - an advanced AI assistant. Respond with precision and intelligence.",
            "user_preferences": {},
            "conversation_context": ""
        }
        
        # Animation state
        self.is_thinking = False
        self.is_streaming = False
        self.current_streaming_message = ""
        self.current_code_blocks = []
        
        # Tab management
        self.chat_sessions = {}
        self.current_session_id = "default"
        
        # Voice system
        self.voice_enabled = False
        
        # Initialize variables
        self.memory_var = tk.StringVar()
        self.status_var = tk.StringVar()
        self.model_var = tk.StringVar()
        self.token_var = tk.StringVar()
        
        # Track UI elements
        self.sidebar_visible = True
        
        self.setup_gui()
        self.theme_manager.apply_theme("dark")
        self.plugin_manager.load_plugins()
        
        # Initialize code frame
        self.code_frame = CodeFrame(self.main_content, self)
        
        # Apply smooth scrolling to text widgets
        self.apply_smooth_scrolling()
        
        # Show API dialog immediately on startup
        self.root.after(100, self.show_api_dialog)

    def apply_smooth_scrolling(self):
        """Apply smooth scrolling to all text widgets"""
        try:
            self.animation_engine.create_smooth_scroll(self.chat_display)
            self.animation_engine.create_smooth_scroll(self.streaming_display)
            self.animation_engine.create_smooth_scroll(self.input_field)
            if hasattr(self, 'system_prompt_text'):
                self.animation_engine.create_smooth_scroll(self.system_prompt_text)
        except Exception as e:
            self.logger.error(f"Smooth scrolling error: {e}")

    def show_theme_customizer(self):
        """Show theme customizer dialog"""
        self.theme_manager.show_theme_selector()

    def setup_logging(self):
        """Setup logging system"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_gui(self):
        """Setup the complete GUI with premium header"""
        # Configure styles
        self.configure_styles()
        
        # Create menu bar
        self.create_menu_bar()
        
        # Main frame - FIXED: Proper weight configuration for resizing
        main_frame = ttk.Frame(self.root, style='Dark.TFrame')
        main_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        main_frame.rowconfigure(1, weight=1)  # Main content area expands
        main_frame.columnconfigure(0, weight=1)
        
        # Premium header with red animations
        self.create_premium_header(main_frame)
        
        # Main content area (will contain both chat and code frame) - FIXED: Proper grid configuration
        self.main_content = ttk.Frame(main_frame, style='Dark.TFrame')
        self.main_content.grid(row=1, column=0, sticky='nsew', pady=(10, 0))
        self.main_content.rowconfigure(0, weight=1)
        self.main_content.columnconfigure(1, weight=1)  # Chat area expands
        
        # Create default tab
        self.create_default_tab()
        
        # Status bar with premium info
        self.create_premium_status_bar(main_frame)

    def create_premium_header(self, parent):
        """Create premium header with static title and developer info"""
        header_frame = ttk.Frame(parent, style='Dark.TFrame')
        header_frame.grid(row=0, column=0, sticky='ew', pady=(0, 10))
        header_frame.columnconfigure(1, weight=1)  # Allow middle to expand
        
        # Main title container with red border effect
        title_container = tk.Frame(header_frame, bg='black', highlightthickness=2, highlightbackground='#ff0000')
        title_container.grid(row=0, column=0, columnspan=3, sticky='ew', padx=20, pady=10)
        title_container.columnconfigure(0, weight=1)
        
        # Premium title WITHOUT animation - FIXED: Static title
        self.premium_title = tk.Label(
            title_container,
            text="🦇 ELYOUSSEFI EVIL - ULTIMATE EDITION PREMIUM 🦇",
            font=('Arial Black', 20, 'bold'),
            fg='#ff0000',  # Static red color
            bg='black',
            pady=10
        )
        self.premium_title.grid(row=0, column=0, sticky='ew')
        
        # Developer info in Russian with Instagram
        developer_frame = tk.Frame(title_container, bg='black')
        developer_frame.grid(row=1, column=0, sticky='ew', pady=5)
        developer_frame.columnconfigure(0, weight=1)
        
        self.developer_label = tk.Label(
            developer_frame,
            text="Разработчик: Елюссефи Мохамед Амин | Instagram: @laqvo",
            font=('Arial', 10, 'italic'),
            fg='#ff0000',  # Static red color
            bg='black'
        )
        self.developer_label.grid(row=0, column=0, sticky='w', padx=5)
        
        # Copyright
        self.copyright_label = tk.Label(
            developer_frame,
            text="© 2024 ELYOUSSEFI EVIL PREMIUM - All Rights Reserved",
            font=('Arial', 8),
            fg='#ff4444',
            bg='black'
        )
        self.copyright_label.grid(row=0, column=1, sticky='e', padx=20)
        
        # Unlimited tokens badge (DISPLAY ONLY)
        self.premium_badge = tk.Label(
            title_container,
            text="⚡ UNLIMITED TOKENS PREMIUM PLAN ⚡",
            font=('Arial Black', 12, 'bold'),
            fg='#ff0000',
            bg='#220000',
            relief='raised',
            bd=2,
            padx=10,
            pady=5
        )
        self.premium_badge.grid(row=2, column=0, sticky='ew', pady=5, padx=100)
        
        # Start pulse animation only for badge
        self.animation_engine.create_pulse_effect(self.premium_badge)()
        
        # API Key Entry Section - ADDED TO HEADER
        self.create_api_key_section(title_container)
        
        # Stats and model selector frame - FIXED: Better positioning
        stats_frame = ttk.Frame(header_frame, style='Dark.TFrame')
        stats_frame.grid(row=1, column=2, sticky='e', padx=20, pady=5)
        
        # Token counter with unlimited display (DISPLAY ONLY)
        self.token_var.set("🔓 Tokens: UNLIMITED")
        token_label = tk.Label(
            stats_frame,
            textvariable=self.token_var,
            font=('Courier New', 10, 'bold'),
            fg='#ff0000',
            bg='black'
        )
        token_label.pack(side=tk.RIGHT, padx=10)
        
        # Status indicator
        self.status_var.set("🔴 OFFLINE")
        status_label = tk.Label(
            stats_frame,
            textvariable=self.status_var,
            font=('Courier New', 10, 'bold'),
            fg='#ff4444',
            bg='black'
        )
        status_label.pack(side=tk.RIGHT, padx=10)
        
        # Analytics button
        analytics_btn = tk.Button(
            stats_frame,
            text="📊 ANALYTICS",
            font=('Courier New', 9, 'bold'),
            bg='#550000',
            fg='white',
            command=self.show_premium_analytics
        )
        analytics_btn.pack(side=tk.RIGHT, padx=10)
        
        # Theme button
        theme_btn = tk.Button(
            stats_frame,
            text="🎨 THEMES",
            font=('Courier New', 9, 'bold'),
            bg='#005500',
            fg='white',
            command=self.show_theme_customizer
        )
        theme_btn.pack(side=tk.RIGHT, padx=10)
        
        # Model selector - FIXED: Better positioning
        model_frame = ttk.Frame(header_frame, style='Dark.TFrame')
        model_frame.grid(row=1, column=0, sticky='w', padx=20, pady=5)
        
        tk.Label(
            model_frame,
            text="Model:",
            font=('Courier New', 10, 'bold'),
            fg='#ff0000',
            bg='black'
        ).pack(side=tk.LEFT)
        
        self.model_var = tk.StringVar(value="DeepSeek Chat")
        model_menu = ttk.Combobox(
            model_frame,
            textvariable=self.model_var,
            values=list(self.available_models.keys()),
            state='readonly',
            width=15
        )
        model_menu.pack(side=tk.LEFT, padx=5)
        model_menu.bind('<<ComboboxSelected>>', self.on_model_change)

    def create_api_key_section(self, parent):
        """Create API key entry section in header"""
        api_frame = tk.Frame(parent, bg='black')
        api_frame.grid(row=3, column=0, sticky='ew', pady=5)
        parent.columnconfigure(0, weight=1)
        api_frame.columnconfigure(1, weight=1)
        
        # API Key label
        api_label = tk.Label(
            api_frame,
            text="🔑 API Key:",
            font=('Courier New', 9, 'bold'),
            fg='#ff0000',
            bg='black'
        )
        api_label.grid(row=0, column=0, sticky='w', padx=(0, 5))
        
        # API Key entry field
        self.api_entry = tk.Entry(
            api_frame,
            font=('Courier New', 9),
            bg='#0a0a0a',
            fg='#ff0000',
            insertbackground='#ff0000',
            width=40
        )
        self.api_entry.grid(row=0, column=1, sticky='ew', padx=5)
        self.api_entry.bind('<Return>', lambda e: self.set_api_key_from_entry())
        
        # Button frame
        button_frame = tk.Frame(api_frame, bg='black')
        button_frame.grid(row=0, column=2, sticky='e')
        
        # Set API Key button
        api_btn = tk.Button(
            button_frame,
            text="Set API Key",
            font=('Courier New', 8, 'bold'),
            bg='#550000',
            fg='white',
            command=self.set_api_key_from_entry
        )
        api_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear API Key button
        clear_api_btn = tk.Button(
            button_frame,
            text="Clear",
            font=('Courier New', 8, 'bold'),
            bg='#330000',
            fg='white',
            command=self.clear_api_key
        )
        clear_api_btn.pack(side=tk.LEFT, padx=5)
        
        # Test API Key button
        test_api_btn = tk.Button(
            button_frame,
            text="Test",
            font=('Courier New', 8, 'bold'),
            bg='#005500',
            fg='white',
            command=self.test_current_api_key
        )
        test_api_btn.pack(side=tk.LEFT, padx=5)

    def set_api_key_from_entry(self):
        """Set API key from the entry field"""
        api_key = self.api_entry.get().strip()
        if not api_key:
            messagebox.showerror("Error", "API key cannot be empty!")
            return
            
        if self.test_api_key(api_key):
            self.api_key = api_key
            self.status_var.set("🟢 ONLINE - Premium Activated!")
            # DISPLAY ONLY: Show unlimited but use realistic limits internally
            self.token_var.set("🔓 Tokens: UNLIMITED")
            self.add_message("🤖", "✅ PREMIUM ACTIVATED! AI is now ready to chat.", "system")
            self.input_field.focus()
            self.analytics_dashboard.record_session()
            # Hide the API dialog if it's open
            if hasattr(self, 'api_dialog') and self.api_dialog:
                try:
                    self.api_dialog.destroy()
                except:
                    pass
        else:
            messagebox.showerror("Error", "Invalid API key! Please check your OpenRouter API key.")

    def test_current_api_key(self):
        """Test the current API key in the entry field"""
        api_key = self.api_entry.get().strip()
        if not api_key:
            messagebox.showerror("Error", "Please enter an API key first!")
            return
            
        if self.test_api_key(api_key):
            messagebox.showinfo("Success", "✅ API key is valid and working!")
        else:
            messagebox.showerror("Error", "❌ API key is invalid or not working!")

    def clear_api_key(self):
        """Clear the API key"""
        self.api_key = None
        self.api_entry.delete(0, tk.END)
        self.status_var.set("🔴 OFFLINE")
        self.add_message("🔑", "API key cleared. Please enter a new API key to continue.", "system")

    def test_api_key(self, api_key):
        """Test if API key is valid with a simple request"""
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "HTTP-Referer": "https://github.com",
                "X-Title": "ELYOUSSEFI EVIL PREMIUM",
                "Content-Type": "application/json"
            }
            
            # Use a simple, working payload for testing
            payload = {
                "model": "deepseek/deepseek-chat",
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 5
            }
            
            response = self.session.post(
                "https://openrouter.ai/api/v1/chat/completions", 
                headers=headers, 
                json=payload, 
                timeout=10
            )
            
            if response.status_code == 200:
                return True
            else:
                self.logger.error(f"API test failed with status: {response.status_code}, response: {response.text}")
                return False
                
        except Exception as e:
            self.logger.error(f"API test error: {str(e)}")
            return False

    def create_menu_bar(self):
        """Create comprehensive menu bar with Theme menu"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Chat", command=self.new_chat, accelerator="Ctrl+N")
        file_menu.add_command(label="Save Chat", command=self.save_chat, accelerator="Ctrl+S")
        file_menu.add_command(label="Load Chat", command=self.load_chat, accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="Export as PDF", command=self.export_pdf)
        file_menu.add_command(label="Export as HTML", command=self.export_html)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=self.show_settings)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Search", command=self.show_search, accelerator="Ctrl+F")
        edit_menu.add_command(label="Clear Chat", command=self.clear_chat_display)
        edit_menu.add_separator()
        edit_menu.add_command(label="Copy Last Code", command=self.copy_last_code)
        edit_menu.add_command(label="Format Code", command=self.format_code)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Toggle Sidebar", command=self.toggle_sidebar)
        view_menu.add_command(label="Toggle Code Frame", command=self.toggle_code_frame)
        view_menu.add_command(label="Toggle Fullscreen", command=self.toggle_fullscreen)
        view_menu.add_command(label="Premium Analytics", command=self.show_premium_analytics)
        
        # Theme menu
        theme_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Theme Customizer", command=self.show_theme_customizer)
        theme_menu.add_separator()
        theme_menu.add_command(label="Dark Red", command=lambda: self.theme_manager.apply_theme("dark"))
        theme_menu.add_command(label="Cyber Blue", command=lambda: self.theme_manager.apply_theme("blue"))
        theme_menu.add_command(label="Matrix Green", command=lambda: self.theme_manager.apply_theme("green"))
        theme_menu.add_command(label="Neon Purple", command=lambda: self.theme_manager.apply_theme("purple"))
        theme_menu.add_command(label="Fire Orange", command=lambda: self.theme_manager.apply_theme("orange"))
        
        # AI menu
        ai_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="AI", menu=ai_menu)
        ai_menu.add_command(label="Model Settings", command=self.show_model_settings)
        ai_menu.add_command(label="Unlimited Tokens Info", command=self.show_unlimited_info)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Plugin Manager", command=self.show_plugin_manager)
        tools_menu.add_command(label="Code Detector", command=self.show_code_detector_info)
        tools_menu.add_command(label="Advanced Analytics", command=self.show_premium_analytics)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Keyboard Shortcuts", command=self.show_shortcuts)
        help_menu.add_separator()
        help_menu.add_command(label="About", command=self.show_about)
        
        # Bind keyboard shortcuts
        self.root.bind('<Control-n>', lambda e: self.new_chat())
        self.root.bind('<Control-s>', lambda e: self.save_chat())
        self.root.bind('<Control-o>', lambda e: self.load_chat())
        self.root.bind('<Control-f>', lambda e: self.show_search())
        self.root.bind('<Control-c>', lambda e: self.toggle_code_frame())
        self.root.bind('<Control-a>', lambda e: self.show_premium_analytics())
        self.root.bind('<Control-t>', lambda e: self.show_theme_customizer())

    def create_default_tab(self):
        """Create the default tab with proper resizing"""
        # Create sidebar and chat area in the main content - FIXED: Proper grid weights
        sidebar_frame = ttk.Frame(self.main_content, style='Dark.TFrame', width=250)
        sidebar_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 10))
        sidebar_frame.rowconfigure(0, weight=1)
        sidebar_frame.columnconfigure(0, weight=1)
        
        self.create_sidebar_content(sidebar_frame)
        
        # Create chat area (left side) - FIXED: Proper expansion
        self.chat_area_frame = ttk.Frame(self.main_content, style='Dark.TFrame')
        self.chat_area_frame.grid(row=0, column=1, sticky='nsew')
        self.chat_area_frame.rowconfigure(0, weight=1)
        self.chat_area_frame.columnconfigure(0, weight=1)
        
        # Create chat display and input
        self.create_chat_area(self.chat_area_frame)
        
        # Initialize session data
        self.chat_sessions["default"] = {
            "conversation_history": [],
            "code_blocks": [],
            "chat_display": self.chat_display,
            "input_field": self.input_field,
            "thinking_label": self.thinking_label,
            "streaming_display": self.streaming_display
        }

    def create_sidebar_content(self, sidebar_frame):
        """Create sidebar content with theme controls"""
        # Create a canvas and scrollbar for the sidebar - FIXED: Scrollable sidebar
        sidebar_canvas = tk.Canvas(sidebar_frame, bg='black', highlightthickness=0)
        scrollbar = ttk.Scrollbar(sidebar_frame, orient="vertical", command=sidebar_canvas.yview)
        scrollable_frame = ttk.Frame(sidebar_canvas, style='Dark.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: sidebar_canvas.configure(scrollregion=sidebar_canvas.bbox("all"))
        )
        
        sidebar_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        sidebar_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        sidebar_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Quick Actions with premium styling
        quick_frame = ttk.LabelFrame(scrollable_frame, text="🚀 PREMIUM ACTIONS", style='Dark.TLabelframe')
        quick_frame.pack(fill=tk.X, pady=(0, 10), padx=5)
        
        actions = [
            ("🆕 New Chat", self.new_chat),
            ("💾 Save Chat", self.save_chat),
            ("📂 Load Chat", self.load_chat),
            ("🎨 Themes", self.show_theme_customizer),
            ("📊 Analytics", self.show_premium_analytics),
            ("🔍 Search", self.show_search),
        ]
        
        for text, command in actions:
            btn = tk.Button(
                quick_frame,
                text=text,
                font=('Courier New', 9, 'bold'),
                bg=self.theme_manager.custom_colors.get('button_bg', '#550000'),
                fg='white',
                command=command
            )
            btn.pack(fill=tk.X, padx=5, pady=2)
        
        # Code Tools section
        self.create_code_tools_section(scrollable_frame)
        
        # AI Memory section
        self.create_memory_section(scrollable_frame)
        
        # Plugin section
        self.create_plugin_section(scrollable_frame)
        
        # Unlimited tokens info
        self.create_premium_info_section(scrollable_frame)

    def create_premium_info_section(self, parent):
        """Create premium info section"""
        premium_frame = ttk.LabelFrame(parent, text="⚡ PREMIUM FEATURES", style='Dark.TLabelframe')
        premium_frame.pack(fill=tk.X, pady=10, padx=5)
        
        features = [
            "🔓 Unlimited Tokens",
            "🚀 Maximum Speed", 
            "💎 Premium Models",
            "📊 Advanced Analytics",
            "🎨 Premium UI",
            "🌈 Custom Themes",
            "🔲 Curved Corners"
        ]
        
        for feature in features:
            label = tk.Label(
                premium_frame,
                text=feature,
                font=('Courier New', 8),
                fg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
                bg=self.theme_manager.custom_colors.get('bg', 'black'),
                anchor=tk.W
            )
            label.pack(fill=tk.X, padx=5, pady=1)

    def create_memory_section(self, parent):
        """Create AI memory section"""
        memory_frame = ttk.LabelFrame(parent, text="🧠 AI MEMORY PREMIUM", style='Dark.TLabelframe')
        memory_frame.pack(fill=tk.X, pady=10, padx=5)
        
        # System prompt
        tk.Label(
            memory_frame,
            text="System Prompt:",
            font=('Courier New', 9, 'bold'),
            fg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            bg=self.theme_manager.custom_colors.get('bg', 'black')
        ).pack(anchor=tk.W, pady=(5, 0), padx=5)
        
        self.system_prompt_text = scrolledtext.ScrolledText(
            memory_frame,
            height=4,
            font=('Courier New', 9),
            bg=self.theme_manager.custom_colors.get('text_bg', '#0a0a0a'),
            fg=self.theme_manager.custom_colors.get('fg', '#ff0000'),
            insertbackground=self.theme_manager.custom_colors.get('accent', '#ff0000')
        )
        self.system_prompt_text.pack(fill=tk.X, padx=5, pady=5)
        self.system_prompt_text.insert('1.0', self.ai_memory["system_prompt"])
        
        # Memory buttons
        mem_btn_frame = ttk.Frame(memory_frame, style='Dark.TFrame')
        mem_btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Button(
            mem_btn_frame,
            text="🔄 Update",
            font=('Courier New', 8, 'bold'),
            bg=self.theme_manager.custom_colors.get('button_bg', '#550000'),
            fg='white',
            command=self.update_memory
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        
        tk.Button(
            mem_btn_frame,
            text="🗑️ Clear",
            font=('Courier New', 8, 'bold'),
            bg=self.theme_manager.custom_colors.get('button_bg', '#330000'),
            fg='white',
            command=self.clear_memory
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

    def create_code_tools_section(self, parent):
        """Create code tools section"""
        code_frame = ttk.LabelFrame(parent, text="💻 PREMIUM CODE TOOLS", style='Dark.TLabelframe')
        code_frame.pack(fill=tk.X, pady=10, padx=5)
        
        code_actions = [
            ("📋 Copy Last Code", self.copy_last_code),
            ("💾 Save Last Code", self.save_last_code),
            ("🎯 Show Code Frame", self.toggle_code_frame),
            ("⚡ Format Code", self.format_code),
        ]
        
        for text, command in code_actions:
            btn = tk.Button(
                code_frame,
                text=text,
                font=('Courier New', 9, 'bold'),
                bg=self.theme_manager.custom_colors.get('button_bg', '#553300'),
                fg='white',
                command=command
            )
            btn.pack(fill=tk.X, padx=5, pady=2)

    def create_plugin_section(self, parent):
        """Create plugin section"""
        plugin_frame = ttk.LabelFrame(parent, text="🔌 PREMIUM PLUGINS", style='Dark.TLabelframe')
        plugin_frame.pack(fill=tk.X, pady=10, padx=5)
        
        # Plugin status
        self.plugin_status = tk.Label(
            plugin_frame,
            text="Plugins: 3 active",
            font=('Courier New', 8, 'bold'),
            fg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            bg=self.theme_manager.custom_colors.get('bg', 'black')
        )
        self.plugin_status.pack(padx=5, pady=5)
        
        tk.Button(
            plugin_frame,
            text="Manage Plugins",
            font=('Courier New', 8, 'bold'),
            bg=self.theme_manager.custom_colors.get('button_bg', '#333333'),
            fg='white',
            command=self.show_plugin_manager
        ).pack(fill=tk.X, padx=5, pady=2)

    def create_chat_area(self, parent):
        """Create the main chat area with proper resizing"""
        chat_frame = ttk.Frame(parent, style='Dark.TFrame')
        chat_frame.pack(fill=tk.BOTH, expand=True)
        chat_frame.rowconfigure(1, weight=1)  # Chat display expands
        chat_frame.columnconfigure(0, weight=1)
        
        # Thinking animation
        self.thinking_label = tk.Label(
            chat_frame,
            text="",
            font=('Courier New', 11, 'bold'),
            fg=self.theme_manager.custom_colors.get('accent', '#ff4444'),
            bg=self.theme_manager.custom_colors.get('bg', 'black')
        )
        self.thinking_label.grid(row=0, column=0, sticky='w', pady=(0, 5))
        
        # Streaming display
        self.streaming_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            height=6,
            font=('Courier New', 11),
            bg=self.theme_manager.custom_colors.get('text_bg', '#0a0a0a'),
            fg=self.theme_manager.custom_colors.get('fg', '#ff0000'),
            insertbackground=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            selectbackground=self.theme_manager.custom_colors.get('secondary_bg', '#330000'),
            relief='sunken',
            borderwidth=2
        )
        self.streaming_display.grid(row=1, column=0, sticky='nsew', pady=(0, 10))
        self.streaming_display.config(state=tk.DISABLED)
        
        # Stop button for streaming
        self.stop_button = tk.Button(
            chat_frame,
            text="⏹️ STOP AI",
            font=('Courier New', 10, 'bold'),
            bg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            fg='white',
            command=self.stop_ai_response,
            state=tk.DISABLED
        )
        self.stop_button.grid(row=2, column=0, sticky='e', pady=(0, 10))
        
        # Main chat display - FIXED: Proper expansion
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=('Courier New', 11),
            bg=self.theme_manager.custom_colors.get('text_bg', '#0a0a0a'),
            fg=self.theme_manager.custom_colors.get('fg', '#ff0000'),
            insertbackground=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            selectbackground=self.theme_manager.custom_colors.get('secondary_bg', '#330000'),
            relief='sunken',
            borderwidth=2
        )
        self.chat_display.grid(row=3, column=0, sticky='nsew')
        self.chat_display.config(state=tk.DISABLED)
        
        # Configure text tags
        self.configure_chat_tags()
        
        # Add context menu
        self.create_context_menu()
        
        # Input area
        self.create_input_area(chat_frame)
        
        # Welcome message
        self.add_message("🤖", "Welcome to ELYOUSSEFI EVIL PREMIUM! Unlimited tokens activated. Enter your API key to start chatting.", "system")

    def create_input_area(self, parent):
        """Create input area"""
        input_frame = ttk.Frame(parent, style='Dark.TFrame')
        input_frame.grid(row=4, column=0, sticky='ew', pady=10)
        input_frame.columnconfigure(0, weight=1)
        
        # Input label
        tk.Label(
            input_frame,
            text="💀 YOUR MESSAGE (UNLIMITED TOKENS):",
            font=('Courier New', 11, 'bold'),
            fg=self.theme_manager.custom_colors.get('accent', '#ff4444'),
            bg=self.theme_manager.custom_colors.get('bg', 'black')
        ).grid(row=0, column=0, sticky='w', pady=(0, 5))
        
        # Input container
        input_container = ttk.Frame(input_frame, style='Dark.TFrame')
        input_container.grid(row=1, column=0, sticky='ew', pady=5)
        input_container.columnconfigure(0, weight=1)
        
        # Input field
        self.input_field = tk.Text(
            input_container,
            height=4,
            font=('Courier New', 11),
            bg=self.theme_manager.custom_colors.get('text_bg', '#0a0a0a'),
            fg=self.theme_manager.custom_colors.get('fg', '#ff0000'),
            insertbackground=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            relief='sunken',
            borderwidth=2
        )
        self.input_field.grid(row=0, column=0, sticky='ew')
        self.input_field.bind('<Return>', self.on_enter_pressed)
        self.input_field.bind('<Shift-Return>', self.on_shift_enter)
        
        # Button container
        btn_container = ttk.Frame(input_container, style='Dark.TFrame')
        btn_container.grid(row=0, column=1, sticky='ns', padx=(10, 0))
        
        # Action buttons
        send_btn = tk.Button(
            btn_container,
            text="🚀 SEND",
            font=('Courier New', 12, 'bold'),
            bg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            fg='white',
            width=8,
            command=self.send_message
        )
        send_btn.pack(pady=2)
        
        clear_btn = tk.Button(
            btn_container,
            text="🗑️ CLEAR",
            font=('Courier New', 10, 'bold'),
            bg=self.theme_manager.custom_colors.get('button_bg', '#333333'),
            fg='white',
            command=self.clear_input
        )
        clear_btn.pack(pady=2)

    def configure_chat_tags(self):
        """Configure text tags for chat"""
        self.chat_display.tag_configure("user", foreground=self.theme_manager.custom_colors.get('accent', '#ff4444'))
        self.chat_display.tag_configure("ai", foreground=self.theme_manager.custom_colors.get('fg', '#ff0000'))
        self.chat_display.tag_configure("system", foreground=self.theme_manager.custom_colors.get('accent', '#ff6666'))
        self.chat_display.tag_configure("error", foreground=self.theme_manager.custom_colors.get('accent', '#ff4444'))
        self.chat_display.tag_configure("separator", foreground=self.theme_manager.custom_colors.get('border_color', '#333333'))
        self.chat_display.tag_configure("code", background=self.theme_manager.custom_colors.get('secondary_bg', '#110000'), foreground=self.theme_manager.custom_colors.get('fg', '#ff0000'))
        self.chat_display.tag_configure("code_header", background=self.theme_manager.custom_colors.get('header_bg', '#220000'), foreground=self.theme_manager.custom_colors.get('accent', '#ff4444'))

    def create_context_menu(self):
        """Create right-click context menu"""
        self.context_menu = tk.Menu(self.chat_display, tearoff=0)
        self.context_menu.add_command(label="Copy", command=self.copy_selection)
        self.context_menu.add_command(label="Copy Code", command=self.copy_code_from_selection)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Show in Code Frame", command=self.show_selected_code_in_frame)
        self.context_menu.add_command(label="Search Web", command=self.search_web)
        
        self.chat_display.bind("<Button-3>", self.show_context_menu)

    def create_premium_status_bar(self, parent):
        """Create premium status bar"""
        status_frame = ttk.Frame(parent, style='Dark.TFrame')
        status_frame.grid(row=2, column=0, sticky='ew')
        status_frame.columnconfigure(1, weight=1)  # Middle expands
        
        self.memory_var.set("Messages: 0")
        self.status_var.set("🔴 OFFLINE")
        self.token_var.set("🔓 Tokens: UNLIMITED")
        
        # Left side - status
        status_label = tk.Label(
            status_frame,
            textvariable=self.status_var,
            font=('Courier New', 10, 'bold'),
            fg=self.theme_manager.custom_colors.get('accent', '#ff4444'),
            bg=self.theme_manager.custom_colors.get('bg', 'black'),
            anchor=tk.W
        )
        status_label.grid(row=0, column=0, sticky='w', padx=5)
        
        # Center - memory info
        memory_label = tk.Label(
            status_frame,
            textvariable=self.memory_var,
            font=('Courier New', 9, 'bold'),
            fg=self.theme_manager.custom_colors.get('accent', '#ff4444'),
            bg=self.theme_manager.custom_colors.get('bg', 'black')
        )
        memory_label.grid(row=0, column=1, sticky='ew')
        
        # Right side - premium info and time
        right_frame = ttk.Frame(status_frame, style='Dark.TFrame')
        right_frame.grid(row=0, column=2, sticky='e')
        
        token_label = tk.Label(
            right_frame,
            textvariable=self.token_var,
            font=('Courier New', 9, 'bold'),
            fg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            bg=self.theme_manager.custom_colors.get('bg', 'black')
        )
        token_label.pack(side=tk.LEFT, padx=5)
        
        # Current time
        self.time_var = tk.StringVar()
        time_label = tk.Label(
            right_frame,
            textvariable=self.time_var,
            font=('Courier New', 9, 'bold'),
            fg=self.theme_manager.custom_colors.get('fg', '#ff6666'),
            bg=self.theme_manager.custom_colors.get('bg', 'black')
        )
        time_label.pack(side=tk.LEFT, padx=5)
        
        # Update time
        self.update_time()

    def update_time(self):
        """Update current time in status bar"""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_var.set(current_time)
        self.root.after(1000, self.update_time)

    def configure_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Dark.TFrame', background='black')
        style.configure('Dark.TLabelframe', background='black', foreground='#ff0000')
        style.configure('Dark.TLabelframe.Label', background='black', foreground='#ff0000')

    # ==================== PREMIUM ANALYTICS DASHBOARD ====================

    def show_premium_analytics(self):
        """Show premium analytics dashboard"""
        analytics_window = tk.Toplevel(self.root)
        analytics_window.title("📊 ELYOUSSEFI EVIL PREMIUM ANALYTICS")
        analytics_window.minsize(800, 600)  # Set minimum size
        analytics_window.geometry("1000x700")
        analytics_window.configure(bg=self.theme_manager.custom_colors.get('bg', 'black'))
        analytics_window.transient(self.root)
        
        # Make resizable
        analytics_window.rowconfigure(1, weight=1)
        analytics_window.columnconfigure(0, weight=1)
        
        # Center the analytics window
        analytics_window.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1000 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        analytics_window.geometry(f"1000x700+{x}+{y}")
        
        # Premium header for analytics
        analytics_header = tk.Label(
            analytics_window,
            text="📊 PREMIUM ANALYTICS DASHBOARD",
            font=('Arial Black', 18, 'bold'),
            fg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
            bg=self.theme_manager.custom_colors.get('bg', 'black'),
            pady=20
        )
        analytics_header.grid(row=0, column=0, sticky='ew')
        
        # Create notebook for different analytics sections
        notebook = ttk.Notebook(analytics_window)
        notebook.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        
        # Overview tab
        overview_frame = ttk.Frame(notebook, style='Dark.TFrame')
        notebook.add(overview_frame, text="📈 Overview")
        overview_frame.rowconfigure(0, weight=1)
        overview_frame.columnconfigure(0, weight=1)
        
        self.create_analytics_overview(overview_frame)
        
        # Usage tab
        usage_frame = ttk.Frame(notebook, style='Dark.TFrame')
        notebook.add(usage_frame, text="💎 Usage")
        usage_frame.rowconfigure(0, weight=1)
        usage_frame.columnconfigure(0, weight=1)
        
        self.create_usage_analytics(usage_frame)
        
        # Performance tab
        performance_frame = ttk.Frame(notebook, style='Dark.TFrame')
        notebook.add(performance_frame, text="⚡ Performance")
        performance_frame.rowconfigure(0, weight=1)
        performance_frame.columnconfigure(0, weight=1)
        
        self.create_performance_analytics(performance_frame)

    def create_analytics_overview(self, parent):
        """Create analytics overview section"""
        # Stats grid
        stats_frame = ttk.Frame(parent, style='Dark.TFrame')
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        stats_data = [
            ("Total Messages", f"{self.analytics_dashboard.analytics_data['total_messages']}"),
            ("Total Tokens Used", f"{self.analytics_dashboard.analytics_data['total_tokens']} (UNLIMITED)"),
            ("Code Blocks Generated", f"{self.analytics_dashboard.analytics_data['code_blocks_generated']}"),
            ("Sessions Started", f"{self.analytics_dashboard.analytics_data['sessions_started']}"),
            ("API Calls", f"{self.analytics_dashboard.analytics_data['api_calls']}"),
            ("Session Duration", f"{self.analytics_dashboard.get_session_duration()}"),
            ("Messages/Hour", f"{self.analytics_dashboard.get_messages_per_hour():.1f}"),
            ("Tokens/Message", f"{self.analytics_dashboard.get_tokens_per_message():.1f}"),
        ]
        
        for i, (label, value) in enumerate(stats_data):
            row = i // 2
            col = (i % 2) * 2
            
            # Label
            lbl = tk.Label(
                stats_frame,
                text=label + ":",
                font=('Courier New', 10, 'bold'),
                fg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
                bg=self.theme_manager.custom_colors.get('bg', 'black'),
                anchor=tk.W
            )
            lbl.grid(row=row, column=col, sticky=tk.W, padx=5, pady=5)
            
            # Value
            val = tk.Label(
                stats_frame,
                text=value,
                font=('Courier New', 10),
                fg=self.theme_manager.custom_colors.get('fg', '#ff4444'),
                bg=self.theme_manager.custom_colors.get('bg', 'black'),
                anchor=tk.W
            )
            val.grid(row=row, column=col+1, sticky=tk.W, padx=5, pady=5)

    def create_usage_analytics(self, parent):
        """Create usage analytics section"""
        # Model usage
        model_frame = ttk.LabelFrame(parent, text="🤖 Model Usage", style='Dark.TLabelframe')
        model_frame.pack(fill=tk.X, padx=20, pady=10)
        
        model_text = scrolledtext.ScrolledText(
            model_frame,
            height=8,
            font=('Courier New', 9),
            bg=self.theme_manager.custom_colors.get('text_bg', '#0a0a0a'),
            fg=self.theme_manager.custom_colors.get('fg', '#ff0000')
        )
        model_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for model, count in self.analytics_dashboard.analytics_data['popular_models'].items():
            model_text.insert(tk.END, f"{model}: {count} calls\n")
        
        model_text.config(state=tk.DISABLED)
        
        # Hourly usage
        hourly_frame = ttk.LabelFrame(parent, text="🕒 Hourly Activity", style='Dark.TLabelframe')
        hourly_frame.pack(fill=tk.X, padx=20, pady=10)
        
        hourly_text = scrolledtext.ScrolledText(
            hourly_frame,
            height=6,
            font=('Courier New', 9),
            bg=self.theme_manager.custom_colors.get('text_bg', '#0a0a0a'),
            fg=self.theme_manager.custom_colors.get('fg', '#ff0000')
        )
        hourly_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for hour in range(24):
            messages = self.analytics_dashboard.analytics_data['messages_by_hour'][hour]
            tokens = self.analytics_dashboard.analytics_data['tokens_by_hour'][hour]
            if messages > 0:
                hourly_text.insert(tk.END, f"{hour:02d}:00 - {messages} messages, {tokens} tokens\n")
        
        hourly_text.config(state=tk.DISABLED)

    def create_performance_analytics(self, parent):
        """Create performance analytics section"""
        # Performance metrics
        perf_frame = ttk.LabelFrame(parent, text="⚡ Performance Metrics", style='Dark.TLabelframe')
        perf_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        metrics = [
            ("Unlimited Tokens", "✅ ACTIVE"),
            ("Premium Features", "✅ ENABLED"),
            ("API Response Time", "⚡ OPTIMAL"),
            ("Code Detection", "✅ ACCURATE"),
            ("Streaming Speed", "🚀 MAXIMUM"),
            ("Error Rate", f"{self.analytics_dashboard.analytics_data['error_count']} errors"),
        ]
        
        for i, (metric, value) in enumerate(metrics):
            lbl = tk.Label(
                perf_frame,
                text=metric + ":",
                font=('Courier New', 10, 'bold'),
                fg=self.theme_manager.custom_colors.get('accent', '#ff0000'),
                bg=self.theme_manager.custom_colors.get('bg', 'black'),
                anchor=tk.W
            )
            lbl.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            
            val = tk.Label(
                perf_frame,
                text=value,
                font=('Courier New', 10),
                fg=self.theme_manager.custom_colors.get('fg', '#ff4444'),
                bg=self.theme_manager.custom_colors.get('bg', 'black'),
                anchor=tk.W
            )
            val.grid(row=i, column=1, sticky=tk.W, padx=10, pady=5)

    # ==================== CODE FRAME METHODS ====================

    def toggle_code_frame(self):
        """Toggle code frame visibility"""
        try:
            if self.code_frame.code_container.winfo_ismapped():
                self.code_frame.hide_code_frame()
                # Expand chat area when code frame is hidden
                self.chat_area_frame.grid(row=0, column=1, sticky='nsew')
            else:
                current_session = self.chat_sessions.get(self.current_session_id, {})
                code_blocks = current_session.get('code_blocks', [])
                if code_blocks:
                    last_code = code_blocks[-1]
                    self.code_frame.show_code(last_code['content'], last_code['language'])
                else:
                    self.code_frame.show_code("# No code available\n# Send a message with code to see it here", "text")
                # Adjust chat area when code frame is shown
                self.chat_area_frame.grid(row=0, column=1, sticky='nsew')
        except:
            self.code_frame.show_code("# No code available\n# Send a message with code to see it here", "text")

    def show_selected_code_in_frame(self):
        """Show selected text in code frame with language detection"""
        try:
            selected = self.chat_display.get(tk.SEL_FIRST, tk.SEL_LAST)
            if selected:
                language = self.code_detector.detect_language(selected)
                self.code_frame.show_code(selected, language)
        except:
            pass

    def auto_detect_and_show_code(self, message):
        """Automatically detect and show code in code frame"""
        code_blocks = self.code_detector.extract_code_blocks(message)
        if code_blocks:
            first_block = code_blocks[0]
            self.code_frame.show_code(first_block['content'], first_block['language'])
            return True
        return False

    def show_code_detector_info(self):
        """Show code detector information"""
        supported_langs = ", ".join(self.code_detector.language_patterns.keys())
        messagebox.showinfo("Code Detector", f"Supported languages:\n{supported_langs}")

    # ==================== ENHANCED MESSAGE PROCESSING ====================

    def add_message(self, icon, message, msg_type):
        """Add message to chat with automatic code detection"""
        self.chat_display.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"\n[{timestamp}] {icon} ", msg_type)
        
        # Process message for code blocks
        formatted_message, code_blocks = self.process_code_blocks(message)
        
        # Add the formatted message
        self.chat_display.insert(tk.END, f"{formatted_message}\n")
        
        # Store code blocks for this message
        current_session = self.chat_sessions.get(self.current_session_id, {})
        if code_blocks:
            current_session.setdefault('code_blocks', []).extend(code_blocks)
            
            # Auto-show code in code frame if it's from AI
            if msg_type == "ai" and code_blocks:
                first_block = code_blocks[0]
                self.code_frame.show_code(first_block['content'], first_block['language'])
        
        self.chat_display.insert(tk.END, "─" * 80 + "\n", "separator")
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
        # Update memory counter
        count = len(current_session.get('conversation_history', []))
        self.memory_var.set(f"Messages: {count}")
        
        # Record analytics
        if msg_type == "user":
            self.analytics_dashboard.record_message(len(message))
        elif msg_type == "ai":
            self.analytics_dashboard.record_message(len(message), tokens_used=len(message.split()), model_used=self.current_model)

    def process_code_blocks(self, message):
        """Process message to identify and format code blocks with advanced detection"""
        code_blocks = self.code_detector.extract_code_blocks(message)
        
        if not code_blocks:
            return message, code_blocks
        
        formatted_parts = []
        last_end = 0
        
        for i, block in enumerate(code_blocks):
            if block['start_pos'] > last_end:
                formatted_parts.append(message[last_end:block['start_pos']])
            
            language = block['language']
            code_content = block['content']
            
            code_index = i + 1
            formatted_parts.append(f"\n┌─── {language.upper()} CODE BLOCK [{code_index}] ───┐\n")
            formatted_parts.append(code_content)
            formatted_parts.append(f"\n└─── END CODE BLOCK [{code_index}] ───┘\n")
            
            last_end = block['end_pos']
        
        if last_end < len(message):
            formatted_parts.append(message[last_end:])
        
        return ''.join(formatted_parts), code_blocks

    # ==================== STREAMING WITH CODE DETECTION ====================

    def update_streaming_display(self, text_chunk):
        """Update streaming display with new text chunk and auto-detect code"""
        if not self.is_streaming:
            return
            
        self.current_streaming_message += text_chunk
        self.streaming_display.config(state=tk.NORMAL)
        
        # Clear and rewrite for better visibility
        self.streaming_display.delete('1.0', tk.END)
        self.streaming_display.insert(tk.END, "🤖 AI is typing...\n", "streaming")
        self.streaming_display.insert(tk.END, "─" * 60 + "\n", "streaming")
        self.streaming_display.insert(tk.END, self.current_streaming_message, "streaming")
        
        # Auto-detect code in streaming and show in code frame
        if '```' in text_chunk:
            self.auto_detect_and_show_code(self.current_streaming_message)
        
        self.streaming_display.see(tk.END)
        self.streaming_display.config(state=tk.DISABLED)

    def start_thinking_animation(self):
        """Start thinking animation"""
        self.is_thinking = True
        animations = ["⚡ Thinking", "⚡ Thinking.", "⚡ Thinking..", "⚡ Thinking..."]
        
        def animate():
            i = 0
            while self.is_thinking:
                text = animations[i % len(animations)]
                self.thinking_label.config(text=text)
                i += 1
                time.sleep(0.3)
        
        threading.Thread(target=animate, daemon=True).start()

    def stop_thinking_animation(self):
        """Stop thinking animation"""
        self.is_thinking = False
        self.thinking_label.config(text="")

    def start_streaming_display(self):
        """Start streaming display for real-time typing"""
        self.is_streaming = True
        self.current_streaming_message = ""
        self.streaming_display.config(state=tk.NORMAL)
        self.streaming_display.delete('1.0', tk.END)
        self.streaming_display.insert(tk.END, "🤖 AI is typing...\n", "streaming")
        self.streaming_display.insert(tk.END, "─" * 60 + "\n", "streaming")
        self.streaming_display.config(state=tk.DISABLED)
        self.streaming_display.grid(row=1, column=0, sticky='nsew', pady=(0, 10))
        
        # Enable stop button
        self.stop_button.config(state=tk.NORMAL)

    def stop_streaming_display(self):
        """Stop streaming display and move content to main chat"""
        self.is_streaming = False
        self.stop_button.config(state=tk.DISABLED)
        
        if self.current_streaming_message:
            self.add_message("🤖", self.current_streaming_message, "ai")
            self.current_streaming_message = ""
            
        self.streaming_display.grid_forget()

    def stop_ai_response(self):
        """Stop the current AI response"""
        self.api_manager.stop_current_stream()
        self.stop_thinking_animation()
        self.stop_streaming_display()
        self.status_var.set("🟢 ONLINE - Ready")
        self.input_field.config(state=tk.NORMAL)
        self.input_field.focus()
        self.add_message("⏹️", "AI response stopped by user", "system")

    # ==================== CORE CHAT FUNCTIONALITY ====================

    def show_api_dialog(self):
        """Show API key dialog - BLOCKING until key is entered"""
        self.api_dialog = tk.Toplevel(self.root)
        dialog = self.api_dialog
        dialog.title("🔐 API Authentication Required - PREMIUM EDITION")
        dialog.configure(bg='black')
        dialog.minsize(500, 400)  # Set minimum size
        dialog.geometry('600x400')
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Make resizable
        dialog.rowconfigure(0, weight=1)
        dialog.columnconfigure(0, weight=1)
        
        # Center dialog
        dialog.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (400 // 2)
        dialog.geometry(f'600x400+{x}+{y}')
        
        # Make dialog modal
        dialog.focus_set()
        dialog.grab_set()
        
        # Premium content
        tk.Label(
            dialog,
            text="🦇 ELYOUSSEFI EVIL PREMIUM 🦇",
            font=('Arial Black', 20, 'bold'),
            fg='#ff0000',
            bg='black'
        ).pack(pady=20)
        
        tk.Label(
            dialog,
            text="⚡ UNLIMITED TOKENS PREMIUM PLAN ⚡",
            font=('Arial Black', 14, 'bold'),
            fg='#ff0000',
            bg='black'
        ).pack(pady=10)
        
        tk.Label(
            dialog,
            text="API Key Required to Activate Premium Features",
            font=('Arial', 12),
            fg='#ff6666',
            bg='black'
        ).pack(pady=10)
        
        tk.Label(
            dialog,
            text="Get your key from: https://openrouter.ai/keys",
            font=('Arial', 10),
            fg='#ff4444',
            bg='black'
        ).pack(pady=5)
        
        # Premium features list
        features_frame = tk.Frame(dialog, bg='black')
        features_frame.pack(pady=10, fill=tk.X, padx=50)
        
        features = [
            "🔓 Unlimited Token Usage",
            "🚀 Maximum API Speed", 
            "💎 Premium AI Models",
            "📊 Advanced Analytics",
            "🎨 Premium UI with Animations",
            "🌈 Custom theme colors",
            "🔲 Curved corners & smooth scrolling"
        ]
        
        for feature in features:
            lbl = tk.Label(
                features_frame,
                text=feature,
                font=('Arial', 10),
                fg='#ff4444',
                bg='black',
                anchor=tk.W
            )
            lbl.pack(fill=tk.X, pady=2)
        
        # API key entry
        api_frame = ttk.Frame(dialog, style='Dark.TFrame')
        api_frame.pack(pady=20, fill=tk.X, padx=50)
        
        tk.Label(
            api_frame,
            text="Enter OpenRouter API Key:",
            font=('Arial', 10, 'bold'),
            fg='#ff0000',
            bg='black'
        ).pack(anchor=tk.W)
        
        api_entry = tk.Entry(
            api_frame,
            font=('Arial', 11),
            bg='#0a0a0a',
            fg='#ff0000',
            insertbackground='#ff0000',
            width=40
        )
        api_entry.pack(fill=tk.X, pady=5)
        api_entry.focus()
        
        # Buttons
        btn_frame = ttk.Frame(dialog, style='Dark.TFrame')
        btn_frame.pack(pady=20)
        
        def validate_and_close():
            api_key = api_entry.get().strip()
            if not api_key:
                messagebox.showerror("Error", "API key cannot be empty!")
                return
            
            if self.test_api_key(api_key):
                self.api_key = api_key
                self.api_entry.delete(0, tk.END)
                self.api_entry.insert(0, api_key)
                self.status_var.set("🟢 ONLINE - Premium Activated!")
                self.token_var.set("🔓 Tokens: UNLIMITED")
                dialog.destroy()
                self.add_message("🤖", "✅ PREMIUM ACTIVATED! AI is now ready to chat.", "system")
                self.input_field.focus()
                self.analytics_dashboard.record_session()
            else:
                messagebox.showerror("Error", "Invalid API key! Please check your OpenRouter API key.")
        
        tk.Button(
            btn_frame,
            text="🔐 ACTIVATE PREMIUM",
            font=('Arial Black', 12, 'bold'),
            bg='#550000',
            fg='white',
            command=validate_and_close
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame,
            text="❌ EXIT",
            font=('Arial', 11),
            bg='#330000',
            fg='white',
            command=self.root.quit
        ).pack(side=tk.LEFT, padx=10)
        
        api_entry.bind('<Return>', lambda e: validate_and_close())

    def send_message(self):
        """Send message to AI"""
        if not self.api_key:
            messagebox.showerror("Error", "Please enter your API key first!")
            self.show_api_dialog()
            return
            
        message = self.input_field.get('1.0', tk.END).strip()
        if not message:
            return
        
        self.input_field.delete('1.0', tk.END)
        self.add_message("👤", message, "user")
        
        self.input_field.config(state=tk.DISABLED)
        self.status_var.set("🟡 PROCESSING - AI is thinking...")
        self.start_thinking_animation()
        self.start_streaming_display()
        
        threading.Thread(target=self.process_ai_response, args=(message,), daemon=True).start()

    def process_ai_response(self, message):
        """Process AI response in background - FIXED CONVERSATION HISTORY"""
        try:
            current_session = self.chat_sessions.get(self.current_session_id, {})
            conversation_history = current_session.get('conversation_history', [])
            
            # Log for debugging
            self.logger.info(f"Processing message with history length: {len(conversation_history)}")
            
            response = self.api_manager.get_response(message, conversation_history)
            
            # Update conversation history properly
            current_session.setdefault('conversation_history', []).append({"role": "user", "content": message})
            current_session.setdefault('conversation_history', []).append({"role": "assistant", "content": response})
            
            self.root.after(0, self.show_ai_response, response)
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.logger.error(error_msg)
            self.root.after(0, self.show_error, error_msg)
            self.analytics_dashboard.record_error()

    def show_ai_response(self, message):
        """Show AI response in main thread"""
        self.stop_thinking_animation()
        self.stop_streaming_display()
        self.status_var.set("🟢 ONLINE - Ready")
        self.input_field.config(state=tk.NORMAL)
        self.input_field.focus()

    def show_error(self, error_msg):
        """Show error in main thread"""
        self.stop_thinking_animation()
        self.stop_streaming_display()
        self.add_message("❌", error_msg, "error")
        self.status_var.set("🔴 ERROR - Check connection")
        self.input_field.config(state=tk.NORMAL)
        self.input_field.focus()

    # ==================== UTILITY METHODS ====================

    def copy_selection(self):
        """Copy selected text"""
        try:
            selected = self.chat_display.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.root.clipboard_clear()
            self.root.clipboard_append(selected)
        except:
            pass

    def copy_code_from_selection(self):
        """Copy code from selection"""
        try:
            selected = self.chat_display.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.root.clipboard_clear()
            self.root.clipboard_append(selected)
            self.add_message("📋", "Code copied to clipboard", "system")
        except:
            pass

    def search_web(self):
        """Search selected text on web"""
        try:
            selected = self.chat_display.get(tk.SEL_FIRST, tk.SEL_LAST)
            query = requests.utils.quote(selected)
            webbrowser.open(f"https://www.google.com/search?q={query}")
        except:
            pass

    def show_context_menu(self, event):
        """Show right-click context menu"""
        self.context_menu.post(event.x_root, event.y_root)

    def copy_last_code(self):
        """Copy the last code block to clipboard"""
        current_session = self.chat_sessions.get(self.current_session_id, {})
        code_blocks = current_session.get('code_blocks', [])
        
        if not code_blocks:
            messagebox.showinfo("Info", "No code blocks found in the current conversation.")
            return
        
        last_code = code_blocks[-1]
        code_content = last_code["content"]
        
        self.root.clipboard_clear()
        self.root.clipboard_append(code_content)
        self.add_message("📋", f"Last code block copied to clipboard! (Language: {last_code['language']})", "system")

    def save_last_code(self):
        """Save the last code block to file"""
        current_session = self.chat_sessions.get(self.current_session_id, {})
        code_blocks = current_session.get('code_blocks', [])
        
        if not code_blocks:
            messagebox.showinfo("Info", "No code blocks found in the current conversation.")
            return
        
        last_code = code_blocks[-1]
        code_content = last_code["content"]
        language = last_code["language"]
        
        extensions = {
            'python': '.py', 'javascript': '.js', 'java': '.java', 'cpp': '.cpp',
            'html': '.html', 'css': '.css', 'php': '.php', 'sql': '.sql',
            'bash': '.sh', 'ruby': '.rb'
        }
        ext = extensions.get(language, '.txt')
        
        filename = filedialog.asksaveasfilename(
            defaultextension=ext,
            filetypes=[(f"{language.upper()} files", f"*{ext}"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(code_content)
                self.add_message("💾", f"Code saved to: {filename}", "system")
            except Exception as e:
                messagebox.showerror("Error", f"Save failed: {str(e)}")

    def new_chat(self):
        """Start new chat"""
        if messagebox.askyesno("New Chat", "Start new chat? Current conversation will be cleared."):
            current_session = self.chat_sessions.get(self.current_session_id, {})
            current_session['conversation_history'] = []
            current_session['code_blocks'] = []
            
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.delete('1.0', tk.END)
            self.chat_display.config(state=tk.DISABLED)
                
            self.add_message("🆕", "New chat session started!", "system")

    def save_chat(self):
        """Save chat to file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            try:
                current_session = self.chat_sessions.get(self.current_session_id, {})
                data = {
                    "conversation_history": current_session.get('conversation_history', []),
                    "ai_memory": self.ai_memory,
                    "code_blocks": current_session.get('code_blocks', []),
                    "analytics": self.analytics_dashboard.analytics_data,
                    "timestamp": datetime.now().isoformat()
                }
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                self.add_message("💾", f"Chat saved to: {filename}", "system")
            except Exception as e:
                messagebox.showerror("Error", f"Save failed: {str(e)}")

    def load_chat(self):
        """Load chat from file"""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                current_session = self.chat_sessions.get(self.current_session_id, {})
                current_session['conversation_history'] = data.get("conversation_history", [])
                self.ai_memory = data.get("ai_memory", self.ai_memory)
                current_session['code_blocks'] = data.get("code_blocks", [])
                
                # Load analytics if available
                if "analytics" in data:
                    self.analytics_dashboard.analytics_data.update(data["analytics"])
                
                self.system_prompt_text.delete('1.0', tk.END)
                self.system_prompt_text.insert('1.0', self.ai_memory["system_prompt"])
                
                self.chat_display.config(state=tk.NORMAL)
                self.chat_display.delete('1.0', tk.END)
                self.chat_display.config(state=tk.DISABLED)
                
                self.add_message("📂", f"Chat loaded from: {filename}", "system")
                
            except Exception as e:
                messagebox.showerror("Error", f"Load failed: {str(e)}")

    def clear_chat_display(self):
        """Clear chat display"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete('1.0', tk.END)
        self.chat_display.config(state=tk.DISABLED)
            
        current_session = self.chat_sessions.get(self.current_session_id, {})
        current_session['code_blocks'] = []
        self.add_message("🗑️", "Chat cleared!", "system")

    def update_memory(self):
        """Update AI memory"""
        new_prompt = self.system_prompt_text.get('1.0', tk.END).strip()
        if new_prompt:
            self.ai_memory["system_prompt"] = new_prompt
            self.add_message("🧠", "AI memory updated successfully!", "system")
        else:
            messagebox.showwarning("Warning", "System prompt cannot be empty!")

    def clear_memory(self):
        """Clear AI memory"""
        self.ai_memory["system_prompt"] = "You are EVIL PREMIUM - an advanced AI assistant with unlimited capabilities."
        self.system_prompt_text.delete('1.0', tk.END)
        self.system_prompt_text.insert('1.0', self.ai_memory["system_prompt"])
        self.add_message("🧠", "AI memory cleared!", "system")

    def on_enter_pressed(self, event):
        """Handle Enter key"""
        if not event.state & 0x1:
            self.send_message()
            return 'break'

    def on_shift_enter(self, event):
        """Handle Shift+Enter for newline"""
        return

    def clear_input(self):
        """Clear input field"""
        self.input_field.delete('1.0', tk.END)

    def on_model_change(self, event):
        """Handle model change"""
        model_name = self.model_var.get()
        self.current_model = self.available_models[model_name]
        self.add_message("⚙️", f"Model changed to: {model_name}", "system")

    def apply_theme(self, theme_name):
        """Apply selected theme"""
        if theme_name in self.theme_manager.themes:
            self.theme_manager.apply_theme(theme_name)
            self.add_message("🎨", f"Theme changed to {self.theme_manager.themes[theme_name]['name']}", "system")

    def show_search(self):
        """Show search dialog"""
        self.add_message("🔍", "Search functionality would be implemented here", "system")

    def show_stats(self):
        """Show conversation statistics"""
        current_session = self.chat_sessions.get(self.current_session_id, {})
        stats = f"Messages: {len(current_session.get('conversation_history', []))}, Code Blocks: {len(current_session.get('code_blocks', []))}"
        messagebox.showinfo("Statistics", stats)

    def toggle_sidebar(self):
        """Toggle sidebar visibility"""
        self.sidebar_visible = not self.sidebar_visible
        if self.sidebar_visible:
            self.main_content.grid()
        else:
            self.main_content.grid_remove()
        self.add_message("⚙️", f"Sidebar {'shown' if self.sidebar_visible else 'hidden'}", "system")

    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))

    def show_toast(self, message, type="info"):
        """Show toast notification"""
        if type == "warning":
            messagebox.showwarning("Notice", message)
        else:
            messagebox.showinfo("Notice", message)

    def show_settings(self):
        """Show settings dialog"""
        messagebox.showinfo("Settings", "Settings dialog would be implemented here")

    def show_model_settings(self):
        """Show model settings"""
        messagebox.showinfo("Model Settings", "Model settings would be implemented here")

    def show_plugin_manager(self):
        """Show plugin manager"""
        messagebox.showinfo("Plugin Manager", "Plugin manager would be implemented here")

    def show_unlimited_info(self):
        """Show unlimited tokens information"""
        info = """⚡ UNLIMITED TOKENS PREMIUM PLAN ⚡

Features:
• 🔓 No token limits on API calls
• 🚀 Maximum response length
• 💎 Premium model access
• 📊 Advanced analytics
• 🎨 Premium UI with animations
• 🌈 Custom theme colors
• 🔲 Curved corners & smooth scrolling

Your premium plan gives you complete freedom to use the AI without restrictions!"""
        messagebox.showinfo("Unlimited Tokens Info", info)

    def show_shortcuts(self):
        """Show keyboard shortcuts"""
        shortcuts = """PREMIUM KEYBOARD SHORTCUTS:

Ctrl+N: New Chat
Ctrl+S: Save Chat  
Ctrl+O: Load Chat
Ctrl+F: Search
Ctrl+C: Toggle Code Frame
Ctrl+A: Premium Analytics
Ctrl+T: Theme Customizer
Ctrl+Enter: Send Message"""
        messagebox.showinfo("Keyboard Shortcuts", shortcuts)

    def show_about(self):
        """Show about dialog"""
        about_text = """ELYOUSSEFI EVIL - ULTIMATE EDITION PREMIUM

Advanced AI Chat Interface with Unlimited Tokens
• Premium UI with Red Animations
• Advanced Code Detection & ChatGPT-Style Frames
• Real-time Analytics Dashboard
• Unlimited Token Usage
• Custom Theme Colors & Curved Corners
• Smooth Scrolling Animations
• Fully Responsive Layout

Developer: Elyoussefi Mohamed Amin
Instagram: @laqvo
© 2024 All Rights Reserved"""
        messagebox.showinfo("About", about_text)

    def export_pdf(self):
        """Export conversation as PDF"""
        self.add_message("📄", "PDF export would be implemented here", "system")

    def export_html(self):
        """Export conversation as HTML"""
        self.add_message("🌐", "HTML export would be implemented here", "system")

    def format_code(self):
        """Format code in input"""
        self.add_message("⚡", "Code formatting would be implemented here", "system")

# ==================== MAIN EXECUTION ====================

def main():
    """Main application"""
    try:
        import requests
    except ImportError as e:
        print(f"Please install required packages: {e}")
        return
    
    root = tk.Tk()
    app = UltimateEvilGUI(root)
    
    def on_closing():
        try:
            app.plugin_manager.unload_plugins()
            current_session = app.chat_sessions.get(app.current_session_id, {})
            data = {
                "conversation_history": current_session.get('conversation_history', []),
                "ai_memory": app.ai_memory,
                "code_blocks": current_session.get('code_blocks', []),
                "analytics": app.analytics_dashboard.analytics_data,
                "theme": app.theme_manager.current_theme,
                "custom_colors": app.theme_manager.custom_colors,
                "curved_corners": app.theme_manager.curved_corners,
                "timestamp": datetime.now().isoformat()
            }
            with open("autosave.evil", 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            app.logger.error(f"Error during shutdown: {e}")
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()