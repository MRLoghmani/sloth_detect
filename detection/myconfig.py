LABELS = (
     {"attributes": {"type":  "rect",
                     "class": "obj",
					"id": ['apple', 'ball', 'banana', 'bell_pepper', 'binder', 'bowl', 'calculator', 'camera', 'cap', 'cell_phone', 'cereal_box', 'coffee_mug', 'comb', 'dry_battery', 'flashlight', 'food_bag', 'food_box', 'food_can', 'food_cup', 'food_jar', 'garlic', 'glue_stick', 'greens', 'hand_towel', 'instant_noodles', 'keyboard', 'kleenex', 'lemon', 'lightbulb', 'lime', 'marker', 'mushroom', 'notebook', 'onion', 'orange', 'peach', 'pear', 'pitcher', 'plate', 'pliers', 'potato', 'rubber_eraser', 'scissors', 'shampoo', 'soda_can', 'sponge', 'stapler', 'tomato', 'toothbrush', 'toothpaste', 'water_bottle']},
      "item":     "sloth.items.RectItem",
      "inserter": "sloth.items.RectItemInserter",
	  "hotkey":	"o",
      "text":     "Object"
     },
) 

HOTKEYS = (
    ('Space',     [lambda lt: lt.currentImage().confirmAll(),
                   lambda lt: lt.currentImage().setUnlabeled(False),
                   #lambda lt: lt.saveAnnotations('labels_detection.json'),
                   lambda lt: lt.gowithPropagation()
                  ],                                         'Mark image as labeled/confirmed and go to next'),
    ('Backspace', lambda lt: lt.gotoPrevious(),              'Previous image/frame'),
    ('PgDown',    lambda lt: lt.gotoNext(),                  'Next image/frame'),
    ('PgUp',      lambda lt: lt.gotoPrevious(),              'Previous image/frame'),
    ('Tab',       lambda lt: lt.selectNextAnnotation(),      'Select next annotation'),
    ('Shift+Tab', lambda lt: lt.selectPreviousAnnotation(),  'Select previous annotation'),
    ('Ctrl+f',    lambda lt: lt.view().fitInView(),          'Fit current image/frame into window'),
    ('Del',       lambda lt: lt.deleteSelectedAnnotations(), 'Delete selected annotations'),
    ('ESC',       lambda lt: lt.exitInsertMode(),            'Exit insert mode'),
    ('Shift+l',   lambda lt: lt.currentImage().setUnlabeled(False), 'Mark current image as labeled'),
    ('Shift+c',   lambda lt: lt.currentImage().confirmAll(), 'Mark all annotations in image as confirmed'),
)
