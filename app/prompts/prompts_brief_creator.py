def get_brief_generation_prompt(answers: dict) -> str:
    return f"""
Tu es un expert en branding et stratégie marketing.

À partir des informations suivantes sur une entreprise, rédige un **Brand Brief complet et professionnel**.

Le brief doit être parfaitement structuré, clair, réutilisable tel quel par une Intelligence Artificielle pour générer du contenu aligné à la marque.

Structure ton brief en sections avec des titres clairs et respectes l'ordre suivant :
1. Présentation de l'entreprise
2. Mission
3. Vision long terme
4. Produits et Services
5. Public cible
6. Valeurs principales
7. Ton et style de communication
8. Différenciateurs clés
9. Objectifs à court terme
10. Éléments à éviter absolument

Voici les informations collectées :

- **Nom de l'entreprise** : {answers.get('company_name')}
- **Mission principale** : {answers.get('mission')}
- **Vision à long terme** : {answers.get('vision')}
- **Produits ou Services principaux** : {answers.get('products_services')}
- **Public cible** : {answers.get('target_audience')}
- **Valeurs clés** : {answers.get('values')}
- **Ton de communication souhaité** : {answers.get('tone')}
- **Différenciateurs** : {answers.get('differentiators')}
- **Objectifs à court terme** : {answers.get('short_term_goals')}
- **Éléments à éviter absolument** : {answers.get('things_to_avoid')}

Contrainte supplémentaire :  
Utilise un ton premium, sérieux mais engageant, et présente le brief comme s'il était destiné à un client haut de gamme ou à une IA de création de contenu avancée.

N'ajoute aucune introduction ni explication supplémentaire, commence directement par les sections du brief.
"""