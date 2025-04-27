#!/bin/bash

echo "🚀 Push des modifications vers GitHub..."

# Vérifier si quelque chose a changé
if git diff --quiet && git diff --cached --quiet; then
  echo "✅ Aucun changement à pusher."
  exit 0
fi

# Ajouter tous les fichiers modifiés
echo "➕ Ajout des fichiers modifiés..."
git add .

# Commit avec un message automatique incluant la date et l'heure
commit_message="push auto - $(date +'%Y-%m-%d %H:%M')"
echo "📝 Commit avec message : $commit_message"
git commit -m "$commit_message"

# Pusher sur la branche principale
echo "📤 Push vers GitHub (branche main)..."
git push origin main || { echo "❌ Erreur lors du git push"; exit 1; }

echo "✅ Push terminé avec succès ! 🎉"