import React from 'react';
import { FilterRule } from '../../types/FilterTypes';

interface FilterRuleListProps {
    rules: FilterRule[];
    onToggleRule: (ruleId: string) => void;
    onDeleteRule: (ruleId: string) => void;
}

export const FilterRuleList: React.FC<FilterRuleListProps> = ({
    rules,
    onToggleRule,
    onDeleteRule
}) => {
    return (
        <div className="space-y-2">
            {rules.map((rule) => (
                <div
                    key={rule.id}
                    className="flex items-center justify-between p-3 bg-white rounded-lg shadow"
                >
                    <div className="flex items-center space-x-3">
                        <input
                            type="checkbox"
                            checked={rule.enabled}
                            onChange={() => onToggleRule(rule.id)}
                            className="h-4 w-4 text-blue-500"
                        />
                        <div>
                            <p className="font-medium">{rule.value}</p>
                            <p className="text-sm text-gray-500">
                                {rule.type} {rule.targetSite && `• ${rule.targetSite}`}
                            </p>
                        </div>
                    </div>
                    <button
                        onClick={() => onDeleteRule(rule.id)}
                        className="text-red-500 hover:text-red-700"
                    >
                        Delete
                    </button>
                </div>
            ))}
        </div>
    );
};