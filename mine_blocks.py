""" If we import mcpi.block we can use names instead of numbers for blocks
"""

from mcpi.minecraft import *
from mcpi.block import *

mc = Minecraft.create()

for i in range(0,100):
    pos = mc.player.getTilePos()
    x = pos.x + 5
    y = pos.y + i
    z = pos.z
    blocktype = LADDER
    mc.setBlock(x, y, z, blocktype)
    mc.setBlock(x+1, y, z, STONE)
    mc.setBlock(x+2, y, z, blocktype)

"""
#TODO
# Make the block appear a short distance from the player
#
# Try these names instead of a number for blockType
#
# AIR, BED, BEDROCK, BEDROCK_INVISIBLE, BOOKSHELF, BRICK_BLOCK, CACTUS,
# CHEST,CLAY, COAL_ORE, COBBLESTONE, COBWEB, CRAFTING_TABLE, DIAMOND_BLOCK,
# DIAMOND_ORE, DIRT, DOOR_IRON, DOOR_WOOD, FARMLAND, FENCE, FENCE_GATE, FIRE,
# FLOWER_CYAN, FLOWER_YELLOW, FURNACE_ACTIVE, FURNACE_INACTIVE, GLASS,
# GLASS_PANE, GLOWSTONE_BLOCK, GOLD_BLOCK, GOLD_ORE, GRASS, GRASS_TALL,
# GRAVEL, ICE, IRON_BLOCK, IRON_ORE, LADDER, LAPIS_LAZULI_BLOCK,
# LAPIS_LAZULI_ORE, LAVA, LAVA_FLOWING, LAVA_STATIONARY, LEAVES, MELON,
# MOSS_STONE, MUSHROOM_BROWN, MUSHROOM_RED, OBSIDIAN,
# REDSTONE_ORE, SAND, SANDSTONE, SAPLING, SNOW, SNOW_BLOCK, STAIRS_COBBLESTONE,
# STAIRS_WOOD, STONE, STONE_BRICK, STONE_SLAB, STONE_SLAB_DOUBLE, SUGAR_CANE,
# TNT, TORCH, WATER, WATER_FLOWING, WATER_STATIONARY, WOOD, WOOD_PLANKS, WOOL
"""
