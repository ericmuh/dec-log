from flask import Blueprint, render_template, redirect, url_for, request


decision_app = Blueprint("decision", __name__, template_folder="templates")
