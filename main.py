import os
import discord
from discord import app_commands
from discord import ui, SelectOption

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

ROLES = {
    "colori": {
        "🤍 White": 1416426078234480841,
        "🖤 Black": 1417131799322300557,
        "🧡 Orange": 1416426109045706892,
        "💙 Blue": 1411413468946632843,
        "💚 Green": 1411413468946632842,
        "💛 Yellow": 1411413468946632841,
        "💜 Purple": 1411413468946632840,
        "🤎 Brown": 1416426058751672502,
        "❤️ Red": 1411413468946632839
    },
    "generi": {
        "👨 Male": 1411413468925399223,
        "👩 Female": 1411413468925399222,
        "❌ Non-binario": 1411413468925399221,
    },
    "giochi": {
        "⚡ Valorant": 1411413468598505572,
        "⛏️ Minecraft": 1411413468598505571,
        "🔫 CS:GO": 1411413468598505570,
        "🏆 Brawl Stars": 1417611381238272001,
        "🎮 Fortnite": 1411413468598505569,
        "🦸 League of Legends": 1411413468598505568,
        "🚓 GTA V": 1411413468598505567
    },
    "notifiche": {
        "📢 Announcements": 1416443338613330044,
        "🎥 Youtube Ping": 1416442776828117093,
        "🎬 Twitch Ping": 1416442770821873877,
    }
}

class RuoliView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    async def handle_role_selection(self, interaction, category, selected_values, max_selections=1):
        for role_id in ROLES[category].values():
            role = interaction.guild.get_role(role_id)
            if role and role in interaction.user.roles:
                await interaction.user.remove_roles(role)
        
        added_roles = []
        for value in selected_values:
            role_id = ROLES[category].get(value)
            if role_id:
                role = interaction.guild.get_role(role_id)
                if role:
                    await interaction.user.add_roles(role)
                    added_roles.append(value)
        
        if added_roles:
            await interaction.response.send_message(f"{category.capitalize()} impostati: {', '.join(added_roles)}", ephemeral=True)
        else:
            await interaction.response.send_message(f"Nessun {category[:-1]} selezionato", ephemeral=True)
    
    @ui.select(placeholder="🎨 Scegli il colore del tuo nome", min_values=1, max_values=1, custom_id="colore_select", options=[SelectOption(label=name, emoji=name.split()[0]) for name in ROLES["colori"].keys()])
    async def colore_callback(self, interaction, select):
        await self.handle_role_selection(interaction, "colori", select.values)
    
    @ui.select(placeholder="👤 Qual è il tuo genere?", min_values=1, max_values=1, custom_id="genere_select", options=[SelectOption(label=name, emoji=name.split()[0]) for name in ROLES["generi"].keys()])
    async def genere_callback(self, interaction, select):
        await self.handle_role_selection(interaction, "generi", select.values)
    
    @ui.select(placeholder="🎮 Quali sono i tuoi giochi preferiti?", min_values=0, max_values=len(ROLES["giochi"]), custom_id="giochi_select", options=[SelectOption(label=name, emoji=name.split()[0]) for name in ROLES["giochi"].keys()])
    async def giochi_callback(self, interaction, select):
        await self.handle_role_selection(interaction, "giochi", select.values, max_selections=len(ROLES["giochi"]))
    
    @ui.select(placeholder="🔔 Quali notifiche vuoi ricevere?", min_values=0, max_values=len(ROLES["notifiche"]), custom_id="notifiche_select", options=[SelectOption(label=name, emoji=name.split()[0]) for name in ROLES["notifiche"].keys()])
    async def notifiche_callback(self, interaction, select):
        await self.handle_role_selection(interaction, "notifiche", select.values, max_selections=len(ROLES["notifiche"]))

@bot.event
async def on_ready():
    print(f'Bot {bot.user} è online!')
    view = RuoliView()
    bot.add_view(view)
    try:
        synced = await tree.sync()
        print(f"Comandi sincronizzati: {len(synced)}")
    except Exception as e:
        print(f"Errore sincronizzazione comandi: {e}")

@tree.command(name="ruoli", description="Scegli i tuoi ruoli preferiti")
async def ruoli(interaction: discord.Interaction):
    embed = discord.Embed(title="SolarGuard APP", description="Scegli i ruoli che preferisci", color=0x00ff00)
    embed.add_field(name="SU DI TE", value="Scegli il colore del tuo nome, il tuo genere e i tuoi giochi preferiti", inline=False)
    embed.add_field(name="NOTIFICHE", value="Scegli quali notifiche vuoi ricevere", inline=False)
    view = RuoliView()
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

bot.run(os.getenv('DISCORD_TOKEN'))
