label start:
    "Welcome to your first debugging challenge. In the fab, things don't always happen as expected."

    "Tools break, tweezers get contaminated, materials change with age, processes turn out to be temperature or humidity dependent..."

    "When something unexpected happens, it's your job as a researcher to figure out why it happened."

    "You might learn something about your materials, your device, or you process. You might also learn that a piece of equipment needs to be repaired or it's time to order fresh chemicals."

    "Virtual debugging challenges are based on actual experiences that have happened in the EE143 lab."

    "You will start with information about the process and the result that raised concern."

    "You'll then be presented with a list of options of actions you might take to proceed."

    "Choose your own adventure!"

label intro:
    scene bg furnace
    "You've finished gate oxidation!"

    "Between cleaning, loading, oxidation, annealing, and unloading, the process took several hours, and you are hungry and tired."

    "You remove the finished wafers and look at the blank witness wafer that you had run as a reference with the patterned wafers."

    "It looks uniformly gray, much like a blank silicon wafer."

    "Oh no! Did you somehow not grow any oxide? Let's find out what happened..."

label choice:
    scene bg cleanroom
menu:
    "Measure the resistivity of the reference wafer":
        jump resistivity

    "Test the hydrophobicity of the reference wafer":
        jump hydrophobic

    "Measure the oxide thickness using the nanospec":
        jump nanospec

    "Inspect the furnace controls":
        jump furnace

    "Declare your answer":
        jump answer

label resistivity:
    scene bg vecco
    "You use the 4-point probe to measure the resistivity of the witness wafer."
    "You have not done an HF dip to remove the oxide."
    "The 4-point probe now reads 9.2E2. The starting wafer had been 2.6E2."
    jump choice

label hydrophobic:
    "You run water from the DI gun in the sink on the wafer."
    "The water spreads out over the surface of the wafer."
    jump choice

label nanospec:
    "You place the witness wafer on the stage of the Nanospec."
    "During set up, you select the program 'Oxide on Silicon.'"
    "When you measure the thickness, you get the following readings:"
    jump choice

label furnace:
    scene bg furnace_ctl
    "You're pretty sure you turned the nitrogen off and oxygen on for the oxidation, then turned it back to oxygen off and nitrogen on for the anneal."
    "You distinctly remember setting the timer and hearing it go off."
    "You ask your lab buddy if they remember you changing the gas flow."
    "Unfortunately, there's no way to go back in time to look at what the oxide flow rate was during the time the wafers were in the furnace."

    "The oxygen for the furnace is supplied by a compressed gas cylinder with a pressure regulator."
    "You inspect the oxygen tank."
    "The gauge for the pressure in the tank is in the green zone (well above 0 psi)."
    "The valves are set to allow gas to flow into the tube."
    "There are no obvious signs of damage to the cylinder itself."
    jump choice

label answer:
    "You decide you know what's going on."
    return
